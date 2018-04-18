from django.views import generic
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from carrier.models import Item 
#from .forms import ItemForm 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
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

#class NewPost(CreateView):
 #   template_name= "newpost.html"

  #  def post(self, request):
   #     if request.method =="POST":
    #        form= ItemForm(request.POST)
     #       if form.is_valid():
      #          post_item = form.save(commit=False)
       #         post_item.save()
        #        args = {'form' : form}
         #    return render(request,'newpost.html',args)

class ProductEntry(CreateView):
    model = Item
    fields = ['item_name', 'sender_name', 'sender_no', 'receiver_name', 'receiver_no', 
            'pickup_place', 'dropoff_place', 'pickup_date', 'delivery_price', 'item_image']
