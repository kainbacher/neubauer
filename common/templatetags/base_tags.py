import re
import os

from django import template
register = template.Library()


@register.simple_tag
def active(request, pattern):
    if re.search(pattern, request.path):
        return 'active'
    return ''


@register.simple_tag
def active_state(request, act):
    if request.path == act:
        return 'active'
    return ''


@register.filter(name='cut')
def cut(value, arg):
    return value.replace(arg, '')


@register.filter(name='replace_with_minus')
def replace_with_minus(value, arg):
    return value.replace(arg, '-')


@register.filter(name='replace_as_linebreak')
def replace_as_linebreak(value, arg):
    return value.replace(arg, '<br/>')


@register.filter(name='replace_as_space')
def replace_as_space(value, arg):
    return value.replace(arg, ' ')


@register.filter
def get_range(value):
    """
    Filter - returns a list containing range made from given value
    Usage (in template):

    <ul>{% for i in 3|get_range %}
      <li>{{ i }}. Do something</li>
    {% endfor %}</ul>

    Results with the HTML:
    <ul>
      <li>0. Do something</li>
      <li>1. Do something</li>
      <li>2. Do something</li>
    </ul>

    Instead of 3 one may use the variable set in the views
    """
    return range(value)


@register.filter(name='url_beautify')
def url_beautify(value):
    value = value.replace('http://', '')
    value = value.replace('/', '')
    return value


@register.filter(name='special_break')
def special_break(value):
    return value.replace('<->', '-<br/>')


@register.filter(name='remove_special_break')
def remove_special_break(value):
    return value.replace('<->', '')
