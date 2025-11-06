from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, Product


class ProfileSerializer(serializers.ModelSerializer):
    """
    用于序列化與反序列化 Profile (擴充的使用者資料)
    """
    class Meta:
        model = Profile
        fields = ['points', 'is_merchant']


class UserSerializer(serializers.ModelSerializer):
    """
    用于序列化與反序列化 User，並內嵌 Profile
    """
    profile = ProfileSerializer(required=False)
    password = serializers.CharField(write_only=True, required=False, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'password',
            'profile',
        ]
        read_only_fields = ['id']

    def create(self, validated_data):
        """
        建立使用者與對應的 Profile
        """
        profile_data = validated_data.pop('profile', {})
        password = validated_data.pop('password', None)

        # 建立 User
        user = User(**validated_data)
        if password:
            user.set_password(password)
        user.save()

        # 建立 Profile（若未提供則建立預設值）
        Profile.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        """
        更新使用者與對應的 Profile
        """
        profile_data = validated_data.pop('profile', {})
        password = validated_data.pop('password', None)

        # 更新基本 User 欄位
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()

        # 更新 Profile 欄位（如果存在）
        profile = getattr(instance, 'profile', None)
        if profile:
            for attr, value in profile_data.items():
                setattr(profile, attr, value)
            profile.save()
        else:
            # 若沒有 Profile（理論上不應發生），則自動建立
            Profile.objects.create(user=instance, **profile_data)

        return instance


class ProductSerializer(serializers.ModelSerializer):
    merchant = serializers.ReadOnlyField(source='merchant.username')

    class Meta:
        model = Product
        fields = [
            'id', 'merchant', 'title', 'description', 'points_required', 'stock', 'created_at'
        ]