from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.urls import reverse


class Profile(models.Model):
    """Extends the built-in User model to include points and merchant flag."""

    # Fields
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    points = models.PositiveIntegerField(default=0, help_text='Current points available for the user.')
    is_merchant = models.BooleanField(default=False, help_text='Designates whether the user is a merchant.')

    # Metadata
    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    # Methods
    def __str__(self):
        """String for representing the Profile object (e.g., in the admin interface)."""
        return f"{self.user.username} - {'Merchant' if self.is_merchant else 'Member'}"

    def get_absolute_url(self):
        """Returns the URL to access this user's profile detail."""
        return reverse('profile')


class Product(models.Model):
    """Represents a redeemable product listed by a merchant."""

    merchant = models.ForeignKey(
        User, 
        on_delete = models.CASCADE,
        related_name = 'products',
        help_text = 'The merchant who listed this product.'
    )
    title = models.CharField(max_length=200, help_text='Product title.')
    description = models.TextField(blank=True, help_text='Product description or details.')
    points_required = models.PositiveIntegerField(help_text='Points required to redeem this product.')
    stock = models.PositiveIntegerField(default=0, help_text='Available stock for redemption.')
    created_at = models.DateTimeField(auto_now_add=True)

    # Metadata
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Product"
        verbose_name_plural = "Products"

    # Methods
    def __str__(self):
        """String for representing the Product object."""
        return f"{self.title} ({self.points_required} pts)"

    def get_absolute_url(self):
        """Returns the URL to access a detail page for this product."""
        return reverse('product-detail', args=[str(self.id)])