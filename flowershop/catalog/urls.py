# catalog/urls.py

from django.urls import path
from .views import product_list

urlpatterns = [
    path('', product_list, name='product_list'),  # URL для главной страницы каталога
]


