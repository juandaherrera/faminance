from django.db import models
from django_userforeignkey.models.fields import UserForeignKey


class BaseModel(models.Model):
    """
    Project main model class

    Args:
        models: django model class
    """

    _deleted = models.BooleanField(
        verbose_name="Borrado", default=False, editable=False
    )
    created_at = models.DateTimeField(
        verbose_name="Fecha de creación", auto_now_add=True, editable=False
    )
    updated_at = models.DateTimeField(
        verbose_name="Fecha de actualización", auto_now=True, editable=False
    )

    created_by = UserForeignKey(
        verbose_name="Creado por",
        auto_user_add=True,
        related_name="+",
        editable=False,
    )
    updated_by = UserForeignKey(
        verbose_name="Actualizado por",
        auto_user=True,
        related_name="+",
        editable=False,
    )

    class Meta:
        abstract = True
