from django.shortcuts import render
from django.views.generic.base import View
from django.template.response   import TemplateResponse


class HomePage(View):
    def get(self, request):
        return render(request, 'index.html')