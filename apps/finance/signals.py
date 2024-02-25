from django.db import transaction as django_transaction
from django.db.models import Q
from django.db.models.signals import post_migrate, post_save, pre_save
from django.dispatch import receiver
from django.utils import timezone

import apps.utils.functions as utils
from apps.users.models import CustomUser

from .input_data import (
    account_type_instaces,
    all_transaction_categories,
    both_categories,
    currency_instances,
)
from .models import (
    Account,
    AccountType,
    Currency,
    Transaction,
    TransactionCategory,
    UserTrasactionCategory,
)


@receiver(post_migrate)
def create_defeault_instances(sender, **kwargs):
    """
    This signal creates the objects defined below when a migration is performed and these objects do not exist.

    In addition, it brings the Representative Market Rate at the time of creation of the instances
    """

    if sender.name == 'apps.finance':
        # --------------- Default Currencies ---------------
        utils.create_objects_from_list(currency_instances, Currency)

        # ----------- Default Account Categories -----------
        utils.create_objects_from_list(account_type_instaces, AccountType)

        # --------- Default Transaction Categories ---------
        utils.create_objects_from_list(all_transaction_categories, TransactionCategory)


@receiver(pre_save, sender=Transaction)
def update_account_balance(sender, instance: Transaction, **kwargs):
    """
    Updates the balance of the account related to an Expense instance after it is saved.
    The balance is updated by subtracting the amount of the expense from the current balance of the account.
    """
    with django_transaction.atomic():
        if instance.pk is None:
            instance.account.balance += instance.amount
        else:
            old_amount = Transaction.objects.get(pk=instance.pk).amount
            old_account = Transaction.objects.get(pk=instance.pk).account
            if instance._deleted:
                old_account.balance -= old_amount
                old_account.save()
                return
            elif old_account != instance.account:
                old_account.balance -= old_amount
                instance.account.balance += instance.amount
                old_account.save()
            elif instance.amount != old_amount:
                instance.account.balance -= float(old_amount)
                instance.account.balance += instance.amount

        instance.account.save()


# @receiver(pre_save, sender=Account)
@receiver(post_save, sender=Account)
def update_account_balance(sender, instance: Account, created, **kwargs):
    if created and instance.balance != 0:
        with django_transaction.atomic():
            amount, instance.balance = instance.balance, 0
            instance.save()
            category, _ = TransactionCategory.objects.get_or_create(**both_categories[0])
            adjustment_cat, _ = UserTrasactionCategory.objects.get_or_create(
                user=instance.user, category=category
            )

            transaction = Transaction.objects.create(
                category=adjustment_cat,
                account=instance,
                amount=amount,
                date=timezone.now(),
                description='Ajuste automático de cuenta',
            )

            transaction.save()


@receiver(post_save, sender=CustomUser)
def default_user_transaction_categories(sender, instance: CustomUser, created, **kwargs):
    user_fg = instance.family_group.all()

    transaction_ctgys = TransactionCategory.objects.filter(
        Q(is_global=True) | Q(family_group__in=user_fg)
    )

    for ctgy in transaction_ctgys:
        try:
            UserTrasactionCategory.objects.get_or_create(user=instance, category=ctgy)
        except Exception as e:
            print(e)
