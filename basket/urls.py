from django.urls import path
from .views import BasketViews

app_name = 'basket'

urlpatterns = [
    path('basket/summary/', BasketViews.basket_summary, name='basket-summary'),
    path('basket/add/', BasketViews.basket_add, name='basket-add'),
    path('basket/delete/', BasketViews.basket_delete, name='basket-delete'),
    path('basket/update/', BasketViews.basket_update, name='basket-update'),
]
