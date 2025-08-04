from django.contrib import admin
from django.urls import path
from products.views import home, product_list, product_detail

from products.views import ProductList, ProductDetail  # API Views
from ai.views import ai_chat

urlpatterns = [
    path('admin/', admin.site.urls),

    # HTML pages
    path('', home, name='home'),
    path('products/', product_list, name='product_list'),
    path('products/<int:pk>/', product_detail, name='product_detail'),

    # API endpoints
    path('api/products/', ProductList.as_view()),
    path('api/products/<int:pk>/', ProductDetail.as_view()),

    
    # AI endpoint without CSRF issues
    path('api/ai/', ai_chat),
]
