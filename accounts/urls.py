# Copied from django.contrib.auth.urls

from django.conf.urls import patterns, url
from django.conf import settings

urlpatterns = patterns('django.contrib.auth.views',
    url(r'^login/$',            'login',                name='login'),
    url(r'^logout/$',           'logout',               name='logout',
                kwargs={'next_page': settings.LOGIN_URL}),
    url(r'^password-change/$',  'password_change',      name='password_change'),
    url(r'^password-changed/$', 'password_change_done', name='password_change_done'),
)
