from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('pricing', views.pricing, name='pricing'),
    path('booksession', views.booksession, name='booksession'),
    path('faqs', views.faqs, name='faqs'),
    path('about', views.about, name='about'),
    path('order', views.order, name='order'),
    path('thankyou', views.thankyou, name='thankyou'),
]