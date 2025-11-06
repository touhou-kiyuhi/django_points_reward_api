from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from ...models import Product
from ...serializers import ProductSerializer


class ProductListCreateView(generics.ListCreateAPIView):
    """
    取得所有商品 (GET)
    建立新商品 (POST)
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer: ProductSerializer) -> None:
        serializer.save(merchant=self.request.user)


class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    取得單一商品 (GET)
    更新商品 (PUT/PATCH)
    刪除商品 (DELETE)
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer: ProductSerializer) -> None:
        product = self.get_object()
        if product.merchant != self.request.user and not self.request.user.is_superuser:
            raise PermissionDenied("你沒有權限修改此商品。")
        serializer.save()

    def perform_destroy(self, instance: Product) -> None:
        if instance.merchant != self.request.user and not self.request.user.is_superuser:
            raise PermissionDenied("你沒有權限刪除此商品。")
        instance.delete()