from django.http import JsonResponse
from .models import Products, Manufacturer


def product_list(request):
    products = Products.objects.all()
    data = {}
    data["products"] = list(products.values())
    response = JsonResponse(data)
    return response

def product_detail(request, pk):
    try:
        product = Products.objects.get(pk=pk)
        data = {}
        data["product"] = {}
        data["name"] = product.name
        data["manufacturer"] = product.manufacturer.name
        data["description"] = product.description
        data["photo"] = product.photo.url
        data["price"] = product.price
        data["shipping_cost"] = product.shipping_cost
        data["quantity"] = product.quantity

        response = JsonResponse(data)
    except Products.DoesNotExist:
        response = JsonResponse({
            "error": {
                "code": 404,
                "message": "Product not found"
            }
        }, status=404)
    return response

def manufacturer_list(request):
    manufacturers = Manufacturer.objects.all().filter(active=True)
    data = {}
    data["manufacturers"] = list(manufacturers.values())
    
    response = JsonResponse(data)
    return response

def manufacturer_detail(request, pk):
    try:
        manufacturer = Manufacturer.objects.get(pk=pk)
        data = {}
        data["name"] = manufacturer.name
        data["location"] = manufacturer.location
        data["active"] = manufacturer.active
        data["products"] = list(manufacturer.products.values())

        response = JsonResponse(data)
    except Manufacturer.DoesNotExist:
        response = JsonResponse({
            "error": {
                "code": 404,
                "message": "Manufacturer not found"
            }
        }, status=404)
        response = JsonResponse(data)
    return response


# commented out http template views
# from django.views.generic.detail import DetailView
# from django.views.generic.list import ListView

# class ProductDetailView(DetailView):
#     model = Products
#     template_name = "products/product_detail.html"


# class ProductListView(ListView):
#     model = Products
#     template_name = "products/product_list.html"
