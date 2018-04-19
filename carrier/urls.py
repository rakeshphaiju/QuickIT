from django.conf.urls import url
from carrier import views
from carrier.views import ItemListView


urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
     url(r'^itemlist/$', views.ItemListView.as_view(),name='item-list'),
     url(r'^profile/$', views.MyProfile.as_view()),
      url(r'^responsibilities/$', views.MyResponsibilities.as_view()),
      url(r'^aboutus/', views.AboutUs.as_view()),
      #url(r'^newpost/$', views.NewPost.as_view(), name='add_post'),
       url(r'^item/entry/$',views.ProductEntry.as_view(),name='product-entry'),
     

]
