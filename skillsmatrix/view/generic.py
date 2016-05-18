from django.views.generic import *
from django.http import JsonResponse

from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect

# def UserRedirectFunctionView(request):
#
#     return HttpResponsePermanentRedirect('/home/?=' + request.query_string)

class UserRedirectView(RedirectView):
    url = '/home/'
    query_string = True
    # permanent = True
    #
    # def get_redirect_url(self, *args, **kwargs):
    #     return '/home/'



















class HomeTemplateView(TemplateView):
    template_name = 'home-template.html'

    def get_context_data(self, **kwargs):
        return {'name': 'TemplateView'}



class AjaxView(FormView):
    def form_invalid(self, form):
        return JsonResponse(form.errors, status=400)

    def form_valid(self, form):
        pass
