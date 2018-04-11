from django.shortcuts import render
from django.views.generic import TemplateView
from carrier.models import Item 

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request):
        return render(request, 'index.html', context=None)


class ItemListView(TemplateView):
    def get(self, request):
        context = {}
        # code to query the database goes here!
        items = Item.objects.all()
        # add data to context
        context["items"] = items
        return render(request, 'itemlist.html', context)

class MyProfile(TemplateView):
    template_name= "profile.html"

class MyResponsibilities(TemplateView):
    template_name= "responsibilities.html"

class AboutUs(TemplateView):
    template_name= "aboutus.html"