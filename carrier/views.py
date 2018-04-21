from django.views import generic
from django.shortcuts import render
from django.views.generic import TemplateView
from carrier.models import Item 
from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


#from .forms import ItemForm 
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

class MyPost(TemplateView):
    def get(self, request):
        context = {}
        # code to query the database goes here!
        items = Item.objects.all()
        # add data to context
        context["items"] = items 
        return render(request, 'mypost.html', context)


class ItemEntry(CreateView):
    model = Item
    fields = ['item_name', 'sender_name', 'sender_no', 'receiver_name', 'receiver_no', 
            'pickup_place', 'dropoff_place', 'pickup_date', 'delivery_price', 'item_image']
# view for deleting a product entry
class ItemDelete(DeleteView):
  model = Item
 # the delete button forwards to the url mentioned below.
  success_url = reverse_lazy('carrier:my-post')

 

# view for the product update page
class ItemUpdate(UpdateView):
    model = Item
    fields = ['item_name', 'sender_name', 'sender_no', 'receiver_name', 'receiver_no', 'pickup_place', 'dropoff_place', 'pickup_date', 'delivery_price', 'item_image']   
 
