from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, FamilyGroup

admin.site.register(FamilyGroup)


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (
            'Custom Info',
            {
                'fields': (
                    'profile_pic',
                    'family_group',
                ),
            },
        ),
    )
