from django.db import models

from apps.users.models import CustomUser, FamilyGroup
from apps.utils.models import BaseModel

from .accounts import Account


class TransactionCategory(BaseModel):
    name = models.CharField(verbose_name='Nombre', max_length=60)
    description = models.TextField(
        verbose_name='Descripción', null=True, blank=True
    )
    icon = models.CharField(
        max_length=80,
        verbose_name='Icono (Fontawesome)',
        default='fa-solid fa-wallet',
    )
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, verbose_name='Parent'
    )
    path = models.TextField(verbose_name='Path', null=True, blank=True)
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, verbose_name='Usuario', null=True
    )
    is_shared = models.BooleanField(
        verbose_name='Cuenta compartida', default=False
    )
    family_group = models.ForeignKey(
        FamilyGroup,
        on_delete=models.CASCADE,
        verbose_name='Grupo Familiar',
        null=True,
    )

    class Meta:
        verbose_name = 'Categoría de Transacción'
        verbose_name_plural = "Categorías de Transacción"
        ordering = ['family_group', 'user', 'name']

        constraints = [
            models.UniqueConstraint(
                fields=['user', 'name', 'parent', 'family_group'],
                name='user_name_parent_family_group_unique_transaction_category',
                condition=models.Q(_deleted=False),
            )
        ]

    def __str__(self):
        if self.parent:
            return f'{self.parent} / {self.name}'
        else:
            return self.name


class Transaction(BaseModel):
    category = models.ForeignKey(
        TransactionCategory, on_delete=models.CASCADE, verbose_name='Categoría'
    )
    account = models.ForeignKey(
        Account, on_delete=models.CASCADE, verbose_name='Cuenta'
    )
    amount = models.DecimalField(
        max_digits=12,
        verbose_name='Valor',
        decimal_places=4,
        null=True,
        blank=True,
        default=0,
    )
    date = models.DateTimeField(verbose_name='Fecha de Transacción')
    description = models.TextField(
        verbose_name='Descripción', null=True, blank=True
    )

    class Meta:
        verbose_name = 'Transacción'
        verbose_name_plural = "Transacciones"
        ordering = ['category', '-date', 'account']

    def __str__(self) -> str:
        return f'({self.category}) | {self.date} | {self.amount}'
