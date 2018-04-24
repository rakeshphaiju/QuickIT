from django.conf import settings
from django.db import models

from carrier.models import Item

User = settings.AUTH_USER_MODEL
# Create your models here.
class ResponsibilityManager(models.Manager):
	def new_or_get(self, request):
		respon_id = request.session.get("respon_id", None)
		qs = self.get_queryset().filter(id=respon_id)
		if qs.count() == 1:
			new_obj = False
			respon_obj = qs.first()
			if request.user.is_authenticated and respon_obj.user is None:
				respon_obj.user = request.user
				respon_obj.save()
		else:
			respon_obj = Responsibility.objects.new_respon(user=request.user)  
			new_obj = True
			request.session['respon_id'] = respon_obj.id
		return respon_obj, new_obj

	def new_respon(self, user=None):
		print(user)
		user_obj = None
		if user is not None:
			if user.is_authenticated:
				user_obj = user
		return self.model.objects.create(user=user_obj)
		

class Responsibility(models.Model):
	user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
	item = models.ManyToManyField(Item, blank=True)
	timestamp =models.DateTimeField(auto_now_add=True)


	objects = ResponsibilityManager()

	def _str_(self):
		return str(self.id)
		


		