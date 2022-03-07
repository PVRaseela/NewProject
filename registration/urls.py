from django.urls import path
from . import views

urlpatterns = [
    path('index',views.home),
    path('hello',views.hellowor)

   
]
