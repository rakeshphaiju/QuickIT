from django.shortcuts import render, redirect
from .models import Responsibility
from carrier.models import Item

def respon_home(request):
	respon_obj = Responsibility.objects.new_or_get(request)
	return render(request, "responsibility/responsibilities.html", {})

def update(request):
	item_id = request.POST.get('item_id')
	if item_id is not None:
		try:
			item_obj = Item.items.get(id=item_id)
		except Item.DoesNotExist:
			print("Show message")
			return redirect("responsibility:home")
		
		respon_obj, new_obj = Responsibility.objects.new_or_get(request)
		if item_obj in respon_obj.items.all():
		 	respon_obj.items.remove(item_obj)
		else: 
			respon_obj.items.add(item_obj)

	return redirect('responsibility:home')
