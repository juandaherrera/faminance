import os

from django.contrib.auth.models import AbstractUser
from django.db import models
from PIL import Image

import apps.utils.constants as const
from apps.utils.models import BaseModel


class FamilyGroup(BaseModel):
    name = models.CharField(max_length=60, verbose_name='Nombre')
    description = models.TextField(null=True, blank=True, verbose_name='Descripción')
    administrator = models.ForeignKey(
        'CustomUser', on_delete=models.CASCADE, verbose_name='Administrador'
    )

    def __str__(self) -> str:
        return f'{self.name}'

    class Meta:
        verbose_name = 'Grupo Familiar'
        verbose_name_plural = 'Grupos Familiares'
        ordering = ['name']


class CustomUser(AbstractUser):
    profile_pic = models.ImageField(
        upload_to='profile_pics/',
        null=True,
        blank=True,
        verbose_name="Foto de Perfil",
    )
    family_group = models.ManyToManyField(FamilyGroup, verbose_name="Grupo Familiar", blank=True)

    def delete_old_image(self) -> None:
        if self.pk and self.profile_pic:
            try:
                old_pic = CustomUser.objects.get(pk=self.pk).profile_pic
                new_pic = self.profile_pic
                if old_pic and old_pic.url != new_pic.url:
                    if os.path.isfile(old_pic.path):
                        os.remove(old_pic.path)
            except CustomUser.DoesNotExist:
                pass

    def resize_image(self) -> None:
        if self.profile_pic:
            img_path = self.profile_pic.path
            img = Image.open(img_path)

            if img.height > const.MAX_IMAGE_HEIGHT:
                output_size = (
                    const.MAX_IMAGE_HEIGHT,
                    int((img.width * const.MAX_IMAGE_HEIGHT) / img.height),
                )
                img = img.resize(output_size, Image.Resampling.LANCZOS)
                img.save(img_path)

    def save(self, *args, **kwargs):
        self.delete_old_image()
        super().save(*args, **kwargs)
        self.resize_image()
