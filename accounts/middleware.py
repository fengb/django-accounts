from django.conf import settings
from django.http import HttpResponseRedirect


class RequireLoginMiddleware(object):
    def process_request(self, request):
        if request.user.is_anonymous() and request.path != settings.LOGIN_URL:
            return HttpResponseRedirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
