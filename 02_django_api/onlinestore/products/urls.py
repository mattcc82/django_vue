from django.urls import path
from .views import (
    manufacturer_detail,
    manufacturer_list,
    product_detail,
    product_list 
    # ProductDetailView, ProductListView
)

urlpatterns = [
    path("products/", product_list, name="product-list"),
    path("products/<int:pk>", product_detail, name="product-detail"),
    path("manufacturers/", manufacturer_list, name="manufacturers-list"),
     path("manufacturers/<int:pk>", manufacturer_detail, name="manufacturers-detail"),
    # path("", ProductListView.as_view(), name="product-list"),
    # path("products/<int:pk>/", ProductDetailView.as_view(), name="product-detail"),
]
