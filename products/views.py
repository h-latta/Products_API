from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Products
from .serializers import ProductSerializer
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
# Create your views here.

class ProductList(APIView):
    def get(self, request, format=None):
            products = Products.objects.all()
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self, request, format=None):
            serializer = ProductSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
class Product_By_ID(APIView):
    def get_object(self, pk):
        product = get_object_or_404(Products, pk=pk)
        return product
    def get(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def put(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    def delete(self, request, pk):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

