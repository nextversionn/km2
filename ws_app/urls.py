from django.urls import path
from ws_app import views

urlpatterns = [
    path('', views.Home),
    path('about/', views.About),
    path('service/', views.Service),
    path('contact/', views.Contact),
]
