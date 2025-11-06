from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    merchant = serializers.ReadOnlyField(source='merchant.username')

    class Meta:
        model = Product
        fields = [
            'id', 'merchant', 'title', 'description', 'points_required', 'stock', 'created_at'
        ]