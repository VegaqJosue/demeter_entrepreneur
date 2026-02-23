import uuid
from django.db import models
from django.core.validators import FileExtensionValidator
from core.current_user import get_current_user


def employee_photo_path(instance, filename):
    # nombre seguro y único: <uuid>.ext
    ext = filename.split('.')[-1].lower()
    return f"employees/photos/{uuid.uuid4().hex}.{ext}"


class Employee(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    # Identificador de la empresa (único en esta instalación)
    employee_code = models.CharField(
        max_length=50,
        unique=True
    )

    # Nombres normalizados
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100, null=True, blank=True)
    third_name = models.CharField(max_length=100, null=True, blank=True)

    first_surname = models.CharField(max_length=100)
    second_surname = models.CharField(max_length=100, null=True, blank=True)

    # Documento legal
    document_name = models.CharField(max_length=50)
    document_id = models.CharField(max_length=50)

    # Foto
    photo = models.ImageField(
        upload_to=employee_photo_path,
        null=True,
        blank=True,
        validators=[FileExtensionValidator(["jpg", "jpeg", "png"])]
    )

    # Límite de crédito permitido
    credit_limit = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    # Auditoría
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        "accounts.User",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="employees_created"
    )

    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(
        "accounts.User",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="employees_updated"
    )

    active = models.BooleanField(default=True)

    class Meta:
        db_table = "employees"
        indexes = [
            models.Index(fields=["employee_code"], name="idx_employee_code"),
            models.Index(fields=["active"], name="idx_employee_active"),
            models.Index(fields=["document_id"], name="idx_employee_national_id"),
        ]

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not self.created_by:
            self.created_by = user
        if user:
            self.updated_by = user
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.first_surname}"
