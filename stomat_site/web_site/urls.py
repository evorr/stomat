from django.urls import path
from .views import about_clinic, price_list, online_entry


urlpatterns = [
    path('', about_clinic, name='about_clinic'),
    path('price/', price_list, name='price_list'),
    path('online/', online_entry, name='online_entry'),
]
