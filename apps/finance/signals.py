from django.db.models.signals import post_migrate, pre_save
from django.dispatch import receiver

from .input_data import account_type_instaces, currency_instances
from .models import AccountType, Currency, Transaction


@receiver(post_migrate)
def create_defeault_instances(sender, **kwargs):
    """
    This signal creates the objects defined below when a migration is performed and these objects do not exist.

    In addition, it brings the Representative Market Rate at the time of creation of the instances
    """

    if sender.name == 'apps.finance':
        # --------------- Default Currencies ---------------
        for c in currency_instances:
            obj, _ = Currency.objects.get_or_create(
                code=c, name=currency_instances[c]
            )

        # --------------- Default Account Categories ---------------
        for ac in account_type_instaces:
            AccountType.objects.get_or_create(
                name=ac,
                description=account_type_instaces[ac]['description'],
                icon=account_type_instaces[ac]['icon'],
            )


@receiver(pre_save, sender=Transaction)
def update_account_balance(sender, instance: Transaction, **kwargs):
    """
    Updates the balance of the account related to an Expense instance after it is saved.
    The balance is updated by subtracting the amount of the expense from the current balance of the account.
    """
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
