from django.test import TestCase
from django.utils import timezone

from apps.users.models import CustomUser

from .models import (
    Account,
    AccountType,
    Currency,
    Transaction,
    TransactionCategory,
    UserTrasactionCategory,
)


class TransactionModelTests(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create(username='Test User', password='TestPassUser123$')
        self.account_type = AccountType.objects.create(name='Test Account Type')
        self.currency = Currency.objects.create(name='Test Money', code='ZZZ')
        self.account = Account.objects.create(
            name="Test Account",
            balance=100.00,
            type=self.account_type,
            currency=self.currency,
            user=self.user,
        )
        self.second_account = Account.objects.create(
            name="Test Account 2",
            balance=50.00,
            type=self.account_type,
            currency=self.currency,
            user=self.user,
        )
        self.category = TransactionCategory.objects.create(name="Test Category")
        self.user_category = UserTrasactionCategory.objects.create(
            user=self.user, category=self.category
        )

    def test_add_new_transaction_updates_account_balance(self):
        amount = 50.00
        Transaction.objects.create(
            category=self.user_category,
            account=self.account,
            amount=amount,
            date=timezone.now(),
            description="Test Transaction",
        )

        self.account.refresh_from_db()

        self.assertEqual(self.account.balance, 150.00)

    def test_edit_transaction_updates_account_balance(self):
        transaction = Transaction.objects.create(
            category=self.user_category,
            account=self.account,
            amount=50.00,
            date=timezone.now(),
            description="Initial Transaction",
        )

        transaction.amount = -50.00
        transaction.save()

        self.account.refresh_from_db()

        self.assertEqual(self.account.balance, 50.00)

    def test_delete_transaction_updates_account_balance(self):
        transaction = Transaction.objects.create(
            category=self.user_category,
            account=self.account,
            amount=50.00,
            date=timezone.now(),
            description="To be deleted",
        )
        transaction_id = transaction.pk
        transaction.delete()

        self.account.refresh_from_db()

        self.assertEqual(self.account.balance, 100.00)

    def test_edit_account_updates_accounts_balances(self):
        transaction = Transaction.objects.create(
            category=self.user_category,
            account=self.account,
            amount=50.00,
            date=timezone.now(),
            description="To be deleted",
        )

        transaction.account = self.second_account
        transaction.save()

        self.account.refresh_from_db()

        self.assertEqual(self.account.balance, 100.00)
        self.assertEqual(self.second_account.balance, 100.00)

    # TO_DO Qué pasa cuando se cambia la cuenta a otra que tiene Currency diferente?


# class AccountModelTests(TestCase):
