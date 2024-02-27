from django import forms

from .models import Account, Transaction


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['type', 'currency', 'name', 'balance', 'is_shared', 'family_group']
        labels = {
            'type': 'Tipo de Cuenta',
            'currency': 'Moneda',
            'name': 'Nombre',
            'balance': 'Saldo',
            'is_shared': 'Cuenta compartida',
            'family_group': 'Grupo Familiar',
        }
        widgets = {
            'type': forms.Select(attrs={'class': 'form-select'}),
            'currency': forms.Select(attrs={'class': 'form-select'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'balance': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_shared': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'family_group': forms.Select(attrs={'class': 'form-select'}),
        }


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['category', 'account', 'amount', 'date', 'description']
        labels = {
            'category': 'Categoría',
            'account': 'Cuenta',
            'amount': 'Monto',
            'date': 'Fecha',
            'description': 'Descripción',
        }
        widgets = {
            'category': forms.Select(attrs={'class': 'form-select'}),
            'account': forms.Select(attrs={'class': 'form-select'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'date': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
