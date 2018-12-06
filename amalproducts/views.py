from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from amalproducts.models import Product
from amalproducts.serializers import ProductSerializer
from rest_framework import generics
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
    queryset = Product.objects.all()
    serializer_class = ProductSerializer  
    permission_classes = (permissions.IsAuthenticated,)

# def product_list(request):
#     """
#     List all code products, or create a new product.
#     """
#     if permissions.IsAuthenticatedOrReadOnly.has_permission: 
#         if request.method == 'GET':
#             products = Product.objects.all()
#             serializer = ProductSerializer(products, many=True)
#             return JsonResponse(serializer.data, safe=False)

#         elif request.method == 'POST':
#             data = JSONParser().parse(request)
#             serializer = ProductSerializer(data=data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return JsonResponse(serializer.data, status=201)
#             return JsonResponse(serializer.errors, status=400)
#     else:
#         return Response({'error': 'prueba'}, status=HTTP_400_BAD_REQUEST)

# def favourites_list(request):
#     """
#     List all code products, or create a new product.
#     """
#     if permissions.IsAuthenticatedOrReadOnly.has_permission:
#         if request.method == 'GET':
#             products = Product.objects.all()
#             serializer = ProductSerializer(products, many=True)
#             return JsonResponse(serializer.data, safe=False)

#         elif request.method == 'POST':
#             data = JSONParser().parse(request)
#             serializer = ProductSerializer(data=data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=201)
#             return JsonResponse(serializer.errors, status=400)
#     else:
#         return Response({'error': 'prueba'}, status=HTTP_400_BAD_REQUEST)