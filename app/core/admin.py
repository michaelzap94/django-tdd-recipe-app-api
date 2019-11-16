from django.contrib import admin

# Import the DEFAULT User admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Convert string in our python to Human readable code.
# Also useful to translate to different languages.
from django.utils.translation import gettext as _

# Import our Models from our 'core' app
from core import models

# Register your models here.


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']

    # SUPPORT ousr CUSTOM User Model

    # Defines the fields and sections that you see for EACH user.
    # Structure: Title for the sections | fields it will contain
    fieldsets = (
        (None, {'fields': ('email', 'password')}),

        (_('Personal Info'), {'fields': ('name',)}),

        (_('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
        }
        ),

        (_('Important dates'), {'fields': ('last_login',)})
    )

    # django: built-in ->
    # -> Defines the fields that you include on the add page(create user page)
    # Structure: Title for the sections | fields it will contain
    add_fieldsets = (
        (None, {
            'classes': ('wide',),  # built-in, default
            'fields': ('email', 'password1', 'password2')
        }),
    )

    #########################################


# Register our custom User model in the django Admin
admin.site.register(models.User, UserAdmin)
