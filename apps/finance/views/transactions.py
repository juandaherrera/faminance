from django.urls import reverse_lazy

from apps.utils.views import (
    BaseCreateView,
    BaseDeleteView,
    BaseListView,
    BaseUpdateView,
)

from ..forms import AccountForm, TransactionForm
from ..models import Transaction


class TransactionListView(BaseListView):
    model = Transaction
    template_name = 'transactions/transaction_list.html'
    breadcrumbs = (
        ('Home', 'core:index'),
        ('Transacciones', None),
    )

    def get_queryset(self):
        return Transaction.objects.filter(account___deleted=False).order_by('-date')


class TransactionCreateView(BaseCreateView):
    model = Transaction
    form_class = TransactionForm
    success_url = reverse_lazy('finance:transaction-list')
    template_name = 'transactions/transaction_form.html'


class TransactionUpdateView(BaseUpdateView):
    model = Transaction
    form_class = TransactionForm
    success_url = reverse_lazy('finance:transaction-list')
    template_name = 'transactions/transaction_form.html'


# TO_DO Lógica para que al borrar una transacción se elimine el monto del balance de la cuenta
class TransactionDeleteView(BaseDeleteView):
    model = Transaction
    success_url = reverse_lazy('finance:transaction-list')
