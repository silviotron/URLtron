from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.url_new, name='url_new'),
    path('show/<str:key>/', views.url_success, name='url_success'),
    path('<str:key>/', views.url_redirect, name='url_redirect'),
]