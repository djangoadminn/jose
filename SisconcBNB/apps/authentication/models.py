from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import ugettext, ugettext_lazy as _
from django.utils import timezone
#from .utils import Selects
# Create your models here.

class AccountManager(BaseUserManager):
    def create_user(self, username, password=None, **kwargs):
        if not username:
            raise ValueError('Users must have a valid username.')

        account = self.model(
            username=self.model.normalize_username(username)
        )

        account.set_password(password)
        account.save()

        return account

    def create_superuser(self, username, password, **kwargs):
        account = self.create_user(username, password, **kwargs)

        account.is_superuser = True
        account.is_staff = True
        account.save()

        return account
class Account(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('username'), max_length=40, primary_key=True, null=False, unique=True)
    ci = models.IntegerField(_('cedula'), null=True, unique=True)
    email = models.EmailField(_('email'))
    first_name = models.CharField(_('first name'), max_length=40)
    last_name = models.CharField(_('last name'), max_length=40)
    birthday = models.DateField(_('fecha nacimiento'), null=True, blank=True)

    is_habitante = models.BooleanField(_('habitante'), default=False)
    is_representante = models.BooleanField(_('representante'), default=False)
    is_coordinador= models.BooleanField(_('coordinador'), default=False)
    is_vocero= models.BooleanField(_('voceros'), default=False)

    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff status'), default=False)
    is_superuser = models.BooleanField(_('superuser status'), default=False)

    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = AccountManager()

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.ci

    def get_full_name(self):
        return ' '.join([self.first_name, self.last_name])

    def get_short_name(self):
        return self.first_name