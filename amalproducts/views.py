from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.contrib.auth.models import User
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from amalproducts.models import Product
from amalproducts.serializers import ProductSerializer
from rest_framework import generics
from rest_framework import filters
from amalproducts.permissions import IsOwner
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (permissions.IsAuthenticated,)

class FavouritesList(generics.ListCreateAPIView):
    serializer_class = ProductSerializer  
    permission_classes = (permissions.IsAuthenticated, IsOwner)
    
    def get_queryset(self):
        return Product.objects.filter(owner=self.request.user)

class MarkingAsFavourite(generics.UpdateAPIView):
    serializer_class = ProductSerializer
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request, product_id, **kwargs):
        instance = Product.objects.get(id=product_id)
        myuser = User.objects.get(id=self.request.user.id)
        instance.owner.add(myuser)
        instance.save()
        return HttpResponse('El producto ' + product_id + ' se ha marcado como favorito')
