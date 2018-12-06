from django.urls import path
from amalproducts import views

urlpatterns = [
    path('1/products/', views.ProductList.as_view()),
    path('1/products/favourites/', views.FavouritesList.as_view()),
]