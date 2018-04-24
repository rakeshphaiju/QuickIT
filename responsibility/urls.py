
from django.conf.urls import url

from .views import (
	respon_home,
	update,
	)


urlpatterns = [
    url(r'^$', respon_home, name='home'),
    url(r'^update/$', update, name='update'),
] 
