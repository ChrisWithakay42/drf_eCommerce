from django.urls import path

from store.views import CategoryDetailView
from store.views import CategoryListView
from store.views import ProductDetailView
from store.views import ProductListView

app_name = 'store'

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<slug:slug>/', CategoryDetailView.as_view(), name='category-detail'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<slug:slug>/', ProductDetailView.as_view(), name='product-detail'),
]