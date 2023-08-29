from rest_framework import generics

from store.models import Category
from store.models import Product
from store.serializers import CategorySerializer
from store.serializers import ProductSerializer


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'


class ProductListView(generics.ListAPIView):
    queryset = Product.products.all()
    serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.products.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'
