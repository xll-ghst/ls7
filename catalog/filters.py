import django_filters
from .models import Product


class ProductFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr="gte")
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr="lte")
    category = django_filters.NumberFilter(field_name="category_id")
    min_stock = django_filters.NumberFilter(field_name="stock", lookup_expr="gte")

    class Meta:
        model = Product
        fields = ["category", "min_price", "max_price", "min_stock"]
