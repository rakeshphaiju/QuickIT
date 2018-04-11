from django.conf.urls import url
from carrier import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
     url(r'^itemlist/$', views.ItemListView.as_view()),
     url(r'^profile/$', views.MyProfile.as_view()),
      url(r'^responsibilities/$', views.MyResponsibilities.as_view()),
      url(r'^aboutus/$', views.AboutUs.as_view()),
]
