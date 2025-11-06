from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth.models import User
from ...models import Profile
from ...serializers import UserSerializer


class UserListCreateView(generics.ListCreateAPIView):
    """
    取得所有使用者 (GET)
    建立新使用者 (POST)
    """
    queryset = User.objects.all().select_related('profile')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]  # 只有管理員能列出或建立使用者

    def perform_create(self, serializer: UserSerializer) -> None:
        serializer.save()


class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    取得單一使用者 (GET)
    更新使用者 (PUT/PATCH)
    刪除使用者 (DELETE)
    """
    queryset = User.objects.all().select_related('profile')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """只允許自己或管理員查看/修改自己的資料"""
        obj = super().get_object()
        if self.request.user != obj and not self.request.user.is_superuser:
            raise PermissionDenied("你沒有權限查看或修改此使用者。")
        return obj

    def perform_update(self, serializer: UserSerializer) -> None:
        user = self.get_object()
        if user != self.request.user and not self.request.user.is_superuser:
            raise PermissionDenied("你沒有權限修改此使用者。")
        serializer.save()

    def perform_destroy(self, instance: User) -> None:
        if instance != self.request.user and not self.request.user.is_superuser:
            raise PermissionDenied("你沒有權限刪除此使用者。")
        instance.delete()
