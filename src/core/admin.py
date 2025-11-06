from django.contrib import admin

# Register your models here.
from core.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Admin view for the Product model."""
    list_display = ('title', 'merchant', 'points_required', 'stock', 'created_at')
    list_filter = ('merchant',)
    search_fields = ('title', 'merchant__username')
    ordering = ('-created_at',)