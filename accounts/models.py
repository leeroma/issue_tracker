from django.contrib.auth.models import AbstractUser
from django.db import models

from accounts.managers import AccountManager


class Account(AbstractUser):
    email = models.EmailField('Адрес электронной почты', unique=True, blank=False, null=False)
    first_name = models.CharField('Имя', max_length=100)
    last_name = models.CharField('Фамилия', max_length=100)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = AccountManager()

    def __str__(self):
        return self.email
