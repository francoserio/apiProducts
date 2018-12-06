from django.urls import path
from amalproducts import views

urlpatterns = [
    path('1/products/', views.product_list),
    path('1/products/favourites/', views.product_list),
]