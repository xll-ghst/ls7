from decimal import Decimal
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Category, Product


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ("username", "email", "password")

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name", "description")


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="category.name", read_only=True)
    final_price = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            "id", "name", "description", "category", "category_name",
            "price", "discount_percent", "final_price",
            "stock", "views_count", "created_at", "updated_at"
        )
        read_only_fields = ("views_count", "created_at", "updated_at")

    def get_final_price(self, obj):
        discount = obj.price * Decimal(obj.discount_percent) / Decimal("100")
        return obj.price - discount

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Цена должна быть больше 0.")
        return value

    def validate_discount_percent(self, value):
        if value > 100:
            raise serializers.ValidationError("Скидка не может быть больше 100%.")
        return value

    def validate(self, attrs):
        if attrs.get("stock", 0) < 0:
            raise serializers.ValidationError({"stock": "Количество не может быть отрицательным."})
        return attrs
