from django.urls import path
from django.conf.urls import url
from amalproducts import views

urlpatterns = [
    path('1/products/', views.ProductList.as_view()),
    path('1/products/favourites/', views.FavouritesList.as_view()),
    url(r'^1/products/(?P<product_id>\d+)/mark_as_favourite/', views.MarkingAsFavourite.as_view())
]