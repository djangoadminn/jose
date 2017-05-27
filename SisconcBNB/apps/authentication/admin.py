from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext, ugettext_lazy as _
from .models import Account

# Register your models here.
# admin.site.register(Account)

@admin.register(Account)
class AccountAdmin(UserAdmin):
    list_display = ('username', 'is_habitante','is_representante','is_coordinador','is_vocero', 'email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_habitante','is_representante','is_coordinador','is_vocero','is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'ci', 'first_name', 'last_name', 'email', 'is_habitante','is_representante','is_coordinador','is_vocero',)
    ordering = ('ci',)
    filter_horizontal = ('groups', 'user_permissions',)

    fieldsets = (
        (None, {'fields': ('username', 'password')  }),
        (_('Personal info'), {'fields': ('ci', 'first_name', 'last_name', 'email','birthday','is_habitante','is_representante','is_coordinador','is_vocero',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'ci', 'first_name', 'last_name', 'email', 'birthday', 'is_habitante', 'is_representante','is_coordinador','is_vocero','password1', 'password2'),
        }),
    )