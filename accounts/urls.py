# Copied from django.contrib.auth.urls

from django.conf.urls import patterns, url
from django.conf import settings

urlpatterns = patterns('django.contrib.auth.views',
    url(r'^login/$', 'login', {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^logout/$', 'logout', {'next_page': settings.LOGIN_URL}, name='logout'),
)
