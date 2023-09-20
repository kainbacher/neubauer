# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView
from cms.sitemaps import CMSSitemap

admin.autodiscover()

urlpatterns = []

sitemaps = {
    'cmspages': CMSSitemap,
    # 'appname': XXSitemap
}

if settings.DEBUG:
    urlpatterns += [
        url(r'^500/', TemplateView.as_view(template_name='500.html')),
        url(r'^404/', TemplateView.as_view(template_name='404.html')),
        url(r'^403/', TemplateView.as_view(template_name='403.html')),
    ]

urlpatterns += [
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('cms.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
