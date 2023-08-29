from rest_framework.serializers import ModelSerializer

from store.models import Category
from store.models import Product


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', 'get_absolute_url')


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        exclude = ['objects', 'products']
