from django.contrib import admin

# Register your models here.
from core.models import Profile, Product


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Admin view for the Profile model."""
    list_display = ('user', 'is_merchant', 'points')
    list_filter = ('is_merchant',)
    search_fields = ('user__username',)
    ordering = ('-points',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Admin view for the Product model."""
    list_display = ('title', 'merchant', 'points_required', 'stock', 'created_at')
    list_filter = ('merchant',)
    search_fields = ('title', 'merchant__username')
    ordering = ('-created_at',)