from django.db import models
from django.utils import timezone

import apps.utils.functions as utils
from apps.users.models import CustomUser, FamilyGroup
from apps.utils.models import BaseModel

from .accounts import Account

TRAN_CAT_TYPE = (
    ('IN', 'Ingreso'),
    ('EX', 'Egreso'),
    ('BO', 'Ambas'),
)


class TransactionCategory(BaseModel):
    name = models.CharField(verbose_name='Nombre', max_length=60)
    description = models.TextField(verbose_name='Descripción', null=True, blank=True)
    icon = models.CharField(
        max_length=80,
        verbose_name='Icono (BootstrapIcon)',
        default='fa-solid fa-wallet',
    )
    type = models.CharField(verbose_name='Tipo', max_length=2, choices=TRAN_CAT_TYPE, default='BO')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, verbose_name='Parent')
    path = models.TextField(verbose_name='Path', null=True, blank=True, editable=False)
    is_global = models.BooleanField(verbose_name='Cuenta compartida', default=False)
    family_group = models.ForeignKey(
        FamilyGroup, on_delete=models.CASCADE, verbose_name='Grupo Familiar', null=True, blank=True
    )

    class Meta:
        verbose_name = 'Categoría de Transacción'
        verbose_name_plural = "Categorías de Transacción"
        ordering = ['family_group', 'name']

        constraints = [
            models.UniqueConstraint(
                fields=['name', 'parent', 'is_global', 'family_group'],
                name='name_parent_is_global_family_group_unique_transaction_category',
                condition=models.Q(_deleted=False),
            )
        ]

    def __str__(self) -> str:
        if self.parent:
            return f'{self.parent} / {self.name}'
        else:
            return self.name


class UserTrasactionCategory(BaseModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Usuario')
    category = models.ForeignKey(
        TransactionCategory, on_delete=models.CASCADE, verbose_name='Categoría'
    )

    class Meta:
        verbose_name = 'Categoría de Transacción Usuario'
        verbose_name_plural = "Categorías de Transacción Usuario"
        ordering = ['user', 'category']

        constraints = [
            models.UniqueConstraint(
                fields=['user', 'category'],
                name='user_category_unique_user_category',
                condition=models.Q(_deleted=False),
            )
        ]

    def __str__(self) -> str:
        return str(self.category)


class Transaction(BaseModel):
    category = models.ForeignKey(
        UserTrasactionCategory, on_delete=models.CASCADE, verbose_name='Categoría'
    )
    account = models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name='Cuenta')
    amount = models.DecimalField(
        max_digits=12,
        verbose_name='Valor',
        decimal_places=4,
        null=True,
        blank=True,
        default=0,
    )
    date = models.DateTimeField(verbose_name='Fecha de Transacción', default=timezone.now)
    description = models.TextField(verbose_name='Descripción', null=True, blank=True)

    @property
    def amount_formatted(self):
        return utils.float_formatter(self.amount)

    class Meta:
        verbose_name = 'Transacción'
        verbose_name_plural = "Transacciones"
        ordering = ['category', '-date', 'account']

    def __str__(self) -> str:
        return f'({self.category}) | {self.date} | {self.amount_formatted}'
