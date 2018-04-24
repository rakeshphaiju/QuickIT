from django.views import generic
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from carrier.models import Item
from django.views import generic
from django.contrib.auth import authenticate, login
from django.views.generic import View, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from responsibility.models import Responsibility
from .forms import UserForm
from django.contrib.auth.decorators import login_required

#from .forms import ItemForm

class HomePageView(TemplateView):
    def get(self, request):
        return render(request, 'login.html', context=None)

class UserFormView(View):
    form_class = UserForm
    template_name ='registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('carrier:item-list')

        return render(request, self.template_name, {'form': form})




        


class ItemListView(TemplateView):
    def get(self, request):
        context = {}
        items = Item.objects.all()
        context["items"] = items
        return render(request, 'itemlist.html', context)

    def get_context_data(self, *args, **kwargs):
        context = super(ItemListView, self).get_context_data(*args, **kwargs)
        respon_obj = Responsibility.objects.new_or_get(self.request)
        context['respon'] = respon_obj
        return context


class MyProfile(TemplateView):
    template_name= "profile.html"

class MyResponsibilities(TemplateView):
    template_name= "responsibilities.html"

class AboutUs(TemplateView):
    template_name= "aboutus.html"


class MyPost(TemplateView):
    def get(self, request):
        context = {}
        items = Item.objects.all()
        context["items"] = items
        return render(request, 'mypost.html', context)


class ItemEntry(CreateView):
    model = Item
    fields = ['item_name', 'sender_name', 'sender_no', 'receiver_name', 'receiver_no',
            'pickup_place', 'dropoff_place', 'pickup_date', 'delivery_price', 'item_image']

class ItemDelete(DeleteView):
  model = Item
  success_url = reverse_lazy('carrier:my-post')

class ItemUpdate(UpdateView):
    model = Item
    fields = ['item_name', 'sender_name', 'sender_no', 'receiver_name', 'receiver_no', 'pickup_place', 'dropoff_place', 'pickup_date', 'delivery_price', 'item_image']
