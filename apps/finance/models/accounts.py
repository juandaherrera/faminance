from django.db import models

from apps.users.models import CustomUser, FamilyGroup
from apps.utils.models import BaseModel


class Currency(BaseModel):
    """
    This model is the representation of different currencies that we will use within the application.
    """

    name = models.CharField(max_length=80, verbose_name='Nombre', unique=True)
    code = models.CharField(max_length=3, verbose_name='Código ISO 4217', unique=True)
    trm = models.DecimalField(
        max_digits=10,
        verbose_name='TRM Value',
        decimal_places=4,
        null=True,
        blank=True,
    )
    trm_updated_at = models.DateTimeField(verbose_name='Last TRM Update', blank=True, null=True)

    class Meta:
        verbose_name = 'Moneda'
        verbose_name_plural = "Monedas"
        ordering = ['code']

    def __str__(self):
        return self.code

    def save(self, *args, **kwargs):
        self.code = self.code.upper()
        super().save(*args, **kwargs)


class AccountType(BaseModel):
    """
    This model is the representation of the account types that users can create.
    For example: savings account, credit cards, assets, liabilities.
    This model will only be accessible to the admin of the application. Users will not be able to create account categories.

    The icons have to be BootstrapIcon classes
    """

    name = models.CharField(max_length=80, verbose_name='Nombre', unique=True)
    description = models.TextField(verbose_name='Descripción', null=True, blank=True)
    icon = models.CharField(
        max_length=80,
        verbose_name='Icono (BootstrapIcon)',
        default='fa-solid fa-wallet',
    )

    class Meta:
        verbose_name = 'Tipo de Cuenta'
        verbose_name_plural = "Tipos de Cuenta"
        ordering = ['name']

    def save(self, *args, **kwargs):
        self.icon = self.icon.lower().strip()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Account(BaseModel):
    """
    This model is the representation of a user account. For example: A savings account at bank x, a credit card at bank y, etc.
    """

    type = models.ForeignKey(AccountType, on_delete=models.CASCADE, verbose_name='Tipo de Cuenta')
    currency = models.ForeignKey(
        Currency, on_delete=models.CASCADE, verbose_name='Moneda'
    )  # , default=1 <- COP debería ser el default
    name = models.CharField(max_length=80, verbose_name='Nombre')
    balance = models.DecimalField(
        max_digits=12,
        verbose_name='Saldo',
        decimal_places=4,
        null=True,
        blank=True,
        default=0,
    )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Usuario')
    is_shared = models.BooleanField(verbose_name='Cuenta compartida', default=False)
    family_group = models.ForeignKey(
        FamilyGroup,
        on_delete=models.CASCADE,
        verbose_name='Grupo Familiar',
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Cuenta'
        verbose_name_plural = "Cuentas"
        ordering = ['family_group', 'user', 'type', 'name']

        constraints = [
            models.UniqueConstraint(
                fields=['user', 'name', 'family_group'],
                name='user_name_family_group_unique_account',
                condition=models.Q(_deleted=False),
            )
        ]

    def __str__(self):
        return f'{self.name} ({self.balance:,.2f} {self.currency})'
