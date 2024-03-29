# Generated by Django 5.0.2 on 2024-02-25 05:04

import django.db.models.deletion
import django_userforeignkey.models.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("finance", "0002_alter_account_options_alter_accounttype_options_and_more"),
        ("users", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="UserTrasactionCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "_deleted",
                    models.BooleanField(
                        default=False, editable=False, verbose_name="Borrado"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Fecha de creación"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Fecha de actualización"
                    ),
                ),
            ],
            options={
                "verbose_name": "Categoría de Transacción Usuario",
                "verbose_name_plural": "Categorías de Transacción Usuario",
                "ordering": ["user", "category"],
            },
        ),
        migrations.AlterModelOptions(
            name="transactioncategory",
            options={
                "ordering": ["family_group", "name"],
                "verbose_name": "Categoría de Transacción",
                "verbose_name_plural": "Categorías de Transacción",
            },
        ),
        migrations.RemoveConstraint(
            model_name="transactioncategory",
            name="user_name_parent_family_group_unique_transaction_category",
        ),
        migrations.RenameField(
            model_name="transactioncategory",
            old_name="is_shared",
            new_name="is_global",
        ),
        migrations.RemoveField(
            model_name="transactioncategory",
            name="user",
        ),
        migrations.AlterField(
            model_name="account",
            name="family_group",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="users.familygroup",
                verbose_name="Grupo Familiar",
            ),
        ),
        migrations.AddConstraint(
            model_name="transactioncategory",
            constraint=models.UniqueConstraint(
                condition=models.Q(("_deleted", False)),
                fields=("name", "parent", "is_global", "family_group"),
                name="name_parent_is_global_family_group_unique_transaction_category",
            ),
        ),
        migrations.AddField(
            model_name="usertrasactioncategory",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="finance.transactioncategory",
                verbose_name="Categoría",
            ),
        ),
        migrations.AddField(
            model_name="usertrasactioncategory",
            name="created_by",
            field=django_userforeignkey.models.fields.UserForeignKey(
                blank=True,
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Creado por",
            ),
        ),
        migrations.AddField(
            model_name="usertrasactioncategory",
            name="updated_by",
            field=django_userforeignkey.models.fields.UserForeignKey(
                blank=True,
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Actualizado por",
            ),
        ),
        migrations.AddField(
            model_name="usertrasactioncategory",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Usuario",
            ),
        ),
        migrations.AlterField(
            model_name="transaction",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="finance.usertrasactioncategory",
                verbose_name="Categoría",
            ),
        ),
    ]
