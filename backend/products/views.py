from django.shortcuts import render, get_object_or_404
from .models import Product
# Create your views here.
def index(request, id):
    print(11111111111)
    # product = Product.objects.get(id=id)
    product = get_object_or_404(Product, id=id)
    context = {
        'product': product,
    }
    return render(request, 'backend_product/index.html', context)
