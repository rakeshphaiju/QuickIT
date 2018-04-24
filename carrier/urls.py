from django.conf.urls import url, include
from carrier import views
from django.conf import settings
from carrier.views import ItemListView
from responsibility.views import respon_home, update

app_name = 'carrier',
app_name = 'responsibility'


urlpatterns = [
    #url(r'^$', views.HomePageView.as_view(),name='index'),
    url(r'^register/$', views.UserFormView.as_view(),name='register'),
    url(r'^$', views.ItemListView.as_view(),name='item-list'),
  url(r'^profile/$', views.MyProfile.as_view()),
  url(r'^responsibilities/', include(('responsibility.urls', 'responsibility'), namespace='responsibility')),
   url(r'^responsibilities/update/', update, name= 'update'),
      url(r'^aboutus/', views.AboutUs.as_view()),
      url(r'^mypost/', views.MyPost.as_view(),name='my-post'),
       url(r'^item/entry/$',views.ItemEntry.as_view(),name='item-entry'),

    url(r'^item/(?P<pk>[0-9]+)/$', views.ItemUpdate.as_view(), name='item-update'),
    url(r'^delete/(?P<pk>[0-9]+)/delete/$', views.ItemDelete.as_view(), name='item-delete'),

]
