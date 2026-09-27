from django.urls import path
from .views import (
    RegisterView,
    CategoryListView,
    ProductListCreateView,
    ProductDetailView,
    TopProductsView,
)

urlpatterns = [
    path("auth/register/", RegisterView.as_view(), name="register"),
    path("categories/", CategoryListView.as_view(), name="categories"),
    path("products/", ProductListCreateView.as_view(), name="products"),
    path("products/top/", TopProductsView.as_view(), name="top-products"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product-detail"),
]
