from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('error/', error, name="index"),
    path('donate/', donate, name="donate"),
    path('order/', check_orderId, name="order")
]