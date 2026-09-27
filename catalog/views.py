from django.core.cache import cache
from django.db.models import F
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .filters import ProductFilter
from .models import Category, Product
from .permissions import IsAdminOrReadOnly
from .serializers import CategorySerializer, ProductSerializer, RegisterSerializer


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.select_related("category").all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]
    filterset_class = ProductFilter
    search_fields = ["name", "description", "category__name"]
    ordering_fields = ["price", "created_at", "views_count", "stock"]
    ordering = ["-created_at"]


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.select_related("category").all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        Product.objects.filter(pk=instance.pk).update(views_count=F("views_count") + 1)
        instance.refresh_from_db()
        return Response(self.get_serializer(instance).data)


class TopProductsView(APIView):
    permission_classes = [permissions.AllowAny]
    CACHE_KEY = "top_products_v1"
    CACHE_TIMEOUT = 60 * 5

    def get(self, request):
        cached = cache.get(self.CACHE_KEY)
        if cached is not None:
            return Response({
                "cached": True,
                "results": cached,
            })

        products = Product.objects.select_related("category").order_by("-views_count", "-created_at")[:10]
        data = ProductSerializer(products, many=True).data

        cache.set(self.CACHE_KEY, data, self.CACHE_TIMEOUT)

        return Response({
            "cached": False,
            "results": data,
        })
