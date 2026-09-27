from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category", "price", "discount_percent", "stock", "views_count")
    list_filter = ("category",)
    search_fields = ("name", "description")
    ordering = ("-created_at",)
