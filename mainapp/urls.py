from django.urls import path
from mainapp import views

urlpatterns = [
    path('', views.home, name="home"),
    path('purchase', views.purchase, name="purchase"),
]
