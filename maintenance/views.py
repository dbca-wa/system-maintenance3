import logging
from django.db.models import Q
from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic.base import View, TemplateView
from django.conf import settings
from django.utils import timezone
from django.views.decorators.csrf import ensure_csrf_cookie
from django import forms
from django.views.generic.base import View, TemplateView
from django.template.loader import get_template
from django.template.loader import render_to_string
from confy import env
from django.http import HttpResponseRedirect

def handler404(request, *args, **kwargs):
    return HttpResponseRedirect('/')

class WaitingPage(TemplateView):
    # preperation to replace old homepage with screen designs..

    template_name = 'maintenance/home.html'
    def render_to_response(self, context):
        PAGE_TYPE = settings.PAGE_TYPE
        
        if PAGE_TYPE is None:
            pass
        else:
            if PAGE_TYPE == 'parkstay':
                self.template_name = 'maintenance/home-parkstay.html'
            if PAGE_TYPE == 'ria':
                self.template_name = 'maintenance/home-ria.html'                

        template = get_template(self.template_name)
        #context['csrf_token_value'] = get_token(self.request)
        response = HttpResponse(template.render(context))
        response["Access-Control-Allow-Headers"] = "*"           
        return response

    def get_context_data(self, **kwargs):
        context = super(WaitingPage, self).get_context_data(**kwargs)        
        context['settings'] = settings
        return context

