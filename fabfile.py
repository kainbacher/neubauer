import time
from fabric.api import env, local, task, cd, prefix, run, lcd
from fabric.colors import green, blue  # red
from fabfile_settings import *


"""
----------------------------------------------------
Fabfile for Djangoeurope Hosted Sites
----------------------------------------------------
Roland Kainbacher
Version     0.8
Date:       09.06.2016
----------------------------------------------------
Change the www, dev variables for your Project

Use this on your local maschine to deploy:
fab deploy
fab deploy:dev

----------------------------------------------------
Use this for cornjob to backup:
fab backup

----------------------------------------------------
Use for download to update the local media and database:
fab update_db

----------------------------------------------------
Future:
Use for download to update the dev media and database:
fab update_to_dev

----------------------------------------------------
"""


def select_env(target):
    """select env."""
    if target == 'dev':
        dev()
    else:
        print 'www'
        www()


def restart_server(folder_name):
    """restart server."""
    if env.server == 'nginx':
        run('~/init/nginx restart')
    else:
        run('~/init/lighttpd reload')
    run('~/init/' + folder_name + ' restart')


def well_done_message(string):
    """well done."""
    print(blue("-------------------------------------------"))
    print(green(" "))
    print(green(" _____ _____ _____ _____ _____ _____ _____ "))
    print(green("|  |  |  _  | __  |  _  |     | __  |  _  |"))
    print(green("|    -|     |    -|     | | | | __ -|     |"))
    print(green("|__|__|__|__|__|__|__|__|_|_|_|_____|__|__|"))
    print(green(" "))
    print(green("%s! Have fun man!" % string))
    print(green(" "))
    print(blue("-------------------------------------------"))


@task
def test():
    """start all tests."""
    local('./manage.py test')


@task
def deploy(target='www', git=False):
    """use this on the server to deploy the new version."""
    # local('./manage.py test')

    if git:
        local('git commit -a')
        local('git push')

    select_env(target)

    with cd(env.dir_code):
        with prefix('source ' + env.dir_vitrualenv):
            run('git pull origin master')
            # run('pip install -r requirements.txt')
            run('./manage.py migrate')
            run('./manage.py collectstatic --noinput')

    restart_server(env.name_folder)
    well_done_message('KARRAMBA CHACKACHAKA - your stuff is live')


@task
def update_db():
    """use this to update the local or dev database and media from server."""
    www()

    date = time.strftime('%Y%m%d%H%M%S')
    bakk_name_media_tar = date + '-backup-media.tar.gz'
    bakk_name_sql = date + '-backup-db.sql'
    bakk_name_sql_tar = date + '-backup-db.sql.tar.gz'

    # cleanup backup folder
    with cd(env.dir_code + '/maintenance/'):
        run('rm -rf backup')
        run('mkdir backup')

    # make backup
    with cd(env.dir_code + '/maintenance/backup/'):
        with prefix('source ' + env.dir_vitrualenv):
            run('pg_dump -U %s %s -f %s'
                % (env.dbuser, env.dbname, bakk_name_sql))

            run('tar -zcvf %s.tar.gz %s' % (bakk_name_sql, bakk_name_sql))
            run('rm -rf %s' % bakk_name_sql)

    # rsync
    local('rsync -rtv beautyparlour@s7.wservices.ch:'
          '/home/beautyparlour/%s/maintenance/backup/ maintenance/backup/'
          % local_name_folder)

    local('rsync -rtv beautyparlour@s7.wservices.ch:'
          '/home/beautyparlour/%s/public/media/ public/media/'
          % local_name_folder)

    # cleanup backup folder
    with cd(env.dir_code + '/maintenance/'):
        run('rm -rf backup')
        run('mkdir backup')

    # unzip and import db
    with lcd('maintenance/backup/'):
        local('tar -zxvf %s' % bakk_name_sql_tar)
        try:
            local('dropdb -h localhost  %s' % local_dbname)
        except:
            pass
        local('createdb -h localhost %s' % local_dbname)
        local('psql -h localhost %s < %s' % (local_dbname, bakk_name_sql))

    # cleanup local backup folder
    with lcd('maintenance/'):
        local('rm -rf backup')
        local('mkdir backup')

    # migrate
    with prefix('source ' + local_dir_vitrualenv):
        local('./manage.py migrate')

    well_done_message('DB & Media Files correctly imported form live Server')


@task
def backup(target='www'):
    """use this on the server to backup the files and database.

    this is just for the cronjob
    fab backup
    fab backup:www
    fab backup:dev
    """
    select_env(target)

    date = time.strftime('%Y%m%d%H%M%S')
    bakk_name_media_zip = date + '-backup-media.zip'
    bakk_name_sql = date + '-backup-db.sql'
    bakk_name_sql_zip = date + '-backup-db.sql.zip'

    # cleanup backup folder
    with lcd('maintenance/'):
        local('rm -rf backup')
        local('mkdir backup')

    with lcd('maintenance/backup/'):

        # bak files
        local('zip -r %s ../../public/media' % bakk_name_media_zip)

        # bak db
        local('pg_dump -U %s %s -f %s' % (
            env.dbuser, env.dbname, bakk_name_sql)
        )
        local('zip -r %s.zip %s' % (bakk_name_sql, bakk_name_sql))
        local('rm -rf %s' % bakk_name_sql)

        local('rsync -avz %s '
              'serveradmin%%beautyparlour.at@s1797.gridserver.com:'
              '/home/1797/users/.home/backups/%s/'
              % (bakk_name_media_zip, env.name_folder))

        local('rsync -rvz %s '
              'serveradmin%%beautyparlour.at@s1797.gridserver.com:'
              '/home/1797/users/.home/backups/%s/'
              % (bakk_name_sql_zip, env.name_folder))

        # remove the files from loacl maschine
        local('rm -rf %s' % bakk_name_media_zip)
        local('rm -rf %s' % bakk_name_sql_zip)
