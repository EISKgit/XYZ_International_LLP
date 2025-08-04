from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.

from rest_framework import generics, filters
from .models import Product
from .serializers import ProductSerializer

# List all products (with filter & sort)
class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'category']
    ordering_fields = ['price', 'rating']


# Get single product details
class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



def home(request):
    # Get filter and sort values from GET params
    category_filter = request.GET.get('category', '')
    sort_value = request.GET.get('sort', '')

    # Start with all products
    products = Product.objects.all()

    # Apply category filter
    if category_filter:
        products = products.filter(category=category_filter)

    # Apply sorting
    if sort_value in ['price', '-price', 'rating', '-rating']:
        products = products.order_by(sort_value)

    # Get unique categories for dropdown
    categories = Product.objects.values_list('category', flat=True).distinct()

    return render(request, 'home.html', {
        'products': products,
        'categories': categories,
        'category_filter': category_filter,
        'sort_value': sort_value
    })




def product_list(request):
    products = Product.objects.all()

    # Filters
    search = request.GET.get('search')
    category = request.GET.get('category')
    sort = request.GET.get('sort')

    if search:
        products = products.filter(name__icontains=search)
    if category:
        products = products.filter(category=category)
    if sort:
        products = products.order_by(sort)

    categories = Product.objects.values_list('category', flat=True).distinct()

    return render(request, 'products.html', {
        'products': products,
        'categories': categories
    })


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})


