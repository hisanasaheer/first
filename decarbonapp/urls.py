from django.urls import path

from decarbonapp import views
app_name='decarbonapp'
urlpatterns = [
    path('', views.index,name='index'),
    path('about/',views.about,name='about'),
    path('blog/',views.blog,name='blog'),
    path('booking/',views.booking,name='booking'),
    path('contact/',views.contact,name='contact'),
    path('flaticon/',views.flaticon,name='flaticon'),
    path('location/',views.location,name='location'),
    path('price/',views.price,name='price'),
    path('service/',views.service,name='service'),
    path('single/',views.single,name='single'),
    path('team/',views.team,name='team'),





]
