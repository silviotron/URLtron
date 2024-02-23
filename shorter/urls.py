from django.urls import path
from . import views

urlpatterns = [
    path('', views.url_new, name='url_new'),
    path('urls/', views.url_list, name='url_list'),
    path('show/<str:key>/', views.url_success, name='url_success'),
    path('<str:key>/', views.url_redirect, name='url_redirect'),
]