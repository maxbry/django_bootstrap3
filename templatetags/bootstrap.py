# -*- coding: utf-8 -*-
# Copyright (C) 2016-1017 Nathanael Philipp (jnphilipp) <mail@jnphilipp.org>
#
# This file is part of django_bootstrap3.
#
# django_bootstrap3 is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# django_bootstrap3 is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with django_bootstrap3. If not, see <http://www.gnu.org/licenses/>.

from django.template import Library
register = Library()


@register.inclusion_tag('bootstrap/css.html')
def bootstrap_css():
    return {}


@register.inclusion_tag('bootstrap/js.html')
def bootstrap_js():
    return {}


@register.inclusion_tag('bootstrap/messages.html', takes_context=True)
def messages(context):
    return {'messages': context['messages']}


@register.inclusion_tag('bootstrap/pagination.html', takes_context=True)
def pagination(context, paginator, page, title=None, *args, **kwargs):
    start_page = max(int(page.number) - 4, 0)
    end_page = min(int(page.number) + 3, paginator.num_pages)
    context['prange'] = paginator.page_range[start_page:end_page]
    context['page'] = page
    context['title'] = title
    context['kwargs'] = kwargs
    return context


@register.inclusion_tag('bootstrap/form/base.html', takes_context=True)
def bootstrap_form(context, form, url='', type='horizontal', **kwargs):
    assert type in ['horizontal', 'inline', 'vertical']
    context['form'] = form
    context['url'] = url
    context['type'] = type
    for k, v in kwargs.items():
        context[k] = v
    return context


@register.inclusion_tag('bootstrap/sortable_th.html', takes_context=True)
def sortable_th(context, column_name, o, get_name, get_value, colspan=1,
                rowspan=1, *args, **kwargs):
    context['column_name'] = column_name
    context['colspan'] = colspan
    context['rowspan'] = rowspan
    context['sort_icon'] = 'up' if o.startswith('-') else 'down'
    context['show_options'] = o.endswith(get_value)

    params = '&'.join(['%s=%s' % (k, v) for k, v in kwargs.items() if v])
    context['link'] = '?%s=%s%s&%s' % (get_name,
                                       '' if o.startswith('-') else '-',
                                       get_value, params)
    context['remove_link'] = '?%s=&%s' % (get_name, params)
    return context
