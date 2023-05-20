from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('about/', views.about, name = 'about'),
    path('faqs/', views.faqs, name = 'faqs'),
    path('news/', views.news, name = 'news'),
    path('login/', views.login, name = 'login'),
    path('resources/', views.resources, name = 'resources'),
    path('waystohelp/', views.waystohelp, name = 'waystohelp')
]