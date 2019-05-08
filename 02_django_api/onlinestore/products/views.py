from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Products, Manufacturer


class ProductDetailView(DetailView):
    model = Products
    template_name = "products/product_detail.html"


class ProductListView(ListView):
    model = Products
    template_name = "products/product_list.html"
