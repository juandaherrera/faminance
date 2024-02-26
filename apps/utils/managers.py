from django.db import models


class NotDeletedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(_deleted=False)
