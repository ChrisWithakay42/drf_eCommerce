from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from store.models import Product
from .basket import Basket
from .serializers import BasketSerializer


class BasketViews(APIView):
    @staticmethod
    def basket_summary(request):
        basket = Basket(request)
        serializer = BasketSerializer({'items': basket.__iter__()})
        return Response(serializer.data)

    @staticmethod
    def basket_add(request):
        basket = Basket(request)
        product_id = int(request.data.get('product_id'))
        product_qty = int(request.data.get('product_qty'))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, qty=product_qty)
        basket.save()
        return Response({'message': 'Product added to the basket successfully.'}, status=status.HTTP_201_CREATED)

    @staticmethod
    def basket_delete(request):
        basket = Basket(request)
        product_id = int(request.data.get('product_id'))
        basket.delete(product=product_id)
        basket.save()
        return Response(
            {'message': 'Product removed from the basket successfully.'},
            status=status.HTTP_204_NO_CONTENT
        )

    @staticmethod
    def basket_update(request):
        basket = Basket(request)
        product_id = int(request.data.get('product_id'))
        product_qty = int(request.data.get('product_qty'))
        basket.update(product=product_id, qty=product_qty)
        basket.save()
        return Response({'message': 'Basket updated successfully.'})
