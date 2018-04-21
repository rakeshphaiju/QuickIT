from django.conf.urls import url
from carrier import views
from carrier.views import ItemListView

app_name = 'carrier'

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(),name='index'),
     url(r'^itemlist/$', views.ItemListView.as_view(),name='item-list'),
     url(r'^profile/$', views.MyProfile.as_view()),
      url(r'^responsibilities/$', views.MyResponsibilities.as_view()),
      url(r'^aboutus/', views.AboutUs.as_view()),
      url(r'^mypost/', views.MyPost.as_view(),name='my-post'),
      #url(r'^newpost/$', views.NewPost.as_view(), name='add_post'),
       url(r'^item/entry/$',views.ItemEntry.as_view(),name='item-entry'),
        
    url(r'^item/(?P<pk>[0-9]+)/$', views.ItemUpdate.as_view(), name='item-update'),
    url(r'^delete/(?P<pk>[0-9]+)/delete/$', views.ItemDelete.as_view(), name='item-delete'),
      
]