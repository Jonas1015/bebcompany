from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('products/', products, name='products'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]
