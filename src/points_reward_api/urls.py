"""
URL configuration for points_reward_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from core.views.api.product_api_view import ProductListCreateView, ProductRetrieveUpdateDestroyView
from core.views.api.userProfile_api_view import UserListCreateView, UserRetrieveUpdateDestroyView

urlpatterns = [
    path('admin/', admin.site.urls),
    # Profile URLs
    path('api/users/', UserListCreateView.as_view(), name='api-user-list-create'),
    path('api/users/<int:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='api-user-detail'),
    # Product URLs
    path('api/products/', ProductListCreateView.as_view(), name='api-product-list'),
    path('api/products/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='api-product-detail'),
]
