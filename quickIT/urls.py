
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from account.views import (login_view, register_view, logout_view)
from quickit import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', login_view, name='login'),
    url(r'^registers/', register_view, name='regis'),
     url(r'^logout/', logout_view, name='logout'),
     url(r'^', include('carrier.urls', namespace='carrier')),
       url(r'^responsibilities/', include(('responsibility.urls', 'responsibility'), namespace='responsibility')),

   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
