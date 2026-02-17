import uuid
from django.db import models
from core.current_user import get_current_user
from django.core.validators import FileExtensionValidator

class Tenant(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    legal_name = models.CharField(
        max_length=150,
        null=False,
        blank=False
    )

    comercial_name = models.CharField(
        max_length=150,
        null=True,
        blank=True
    )

    logo_url = models.ImageField(
        upload_to="tenants/logos/",
        null=True,
        blank=True,
        validators=[FileExtensionValidator(["jpg","jpeg"])]
    )

    default_currency = models.CharField(
        max_length=3,
        default="USD",
        null=False,
        blank=False
    )

    timezone = models.CharField(
        max_length=100,
        default='UTC',
        null=False,
        blank=False
    )

    created_at = models.DateTimeField(auto_now_add=True)

    created_by = models.ForeignKey(
        'accounts.User',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='tenants_created'
    )

    updated_at = models.DateField(auto_now=True)

    updated_by = models.ForeignKey(
        'accounts.User',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='tenants_updated'
    )

    active = models.BooleanField(default=True)

    class Meta:
        db_table = "tenants"
        indexes = [
            models.Index(fields=["active"], name="idx_tenants_active")
        ]
        verbose_name = "Tenant"
        verbose_name_plural = "Tenants"
    
    def __str__(self):
        return self.comercial_name
    
    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not self.created_by:
            self.created_by = user
        if user:
            self.updated_by = user
        super().save(*args, **kwargs)
