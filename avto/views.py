from django.shortcuts import render
from django.views.generic import TemplateView


class Start(TemplateView):
    template_name = 'start.html'