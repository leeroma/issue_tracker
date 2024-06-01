from django.db import models

from accounts.models import Account
from issuetracker.form_validators import StatusValidator, validate_language, check_len


class Status(models.Model):
    SYMBOLS = ".,:;?!/()[]{}@#&"
    name = models.CharField(max_length=100, null=False, blank=False, unique=True, validators=[StatusValidator(SYMBOLS)])

    class Meta:
        verbose_name_plural = 'Statuses'

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField('Название', max_length=100, null=False, blank=False, validators=[validate_language, ])
    description = models.TextField('Описание', max_length=3000, null=True, blank=True, validators=[validate_language, ])
    user = models.ManyToManyField(Account, verbose_name='Пользователь', related_name='projects')
    start = models.DateField('Дата начала', null=False, blank=False)
    deadline = models.DateField('Дата окончания', blank=True, null=True)

    def __str__(self):
        return self.name


class Issue(models.Model):
    summary = models.CharField('Заголовок', max_length=100, null=False, blank=False,
                               validators=[validate_language, check_len, ])
    description = models.TextField('Описание', max_length=3000, null=True, blank=True, validators=[validate_language, ])
    status = models.ForeignKey(Status, on_delete=models.PROTECT, related_name='status', verbose_name='Статус')
    type = models.ForeignKey(Type, on_delete=models.PROTECT, related_name='type', verbose_name='Тип')

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='issues', verbose_name='Проект',
                                default=1)
    is_deleted = models.BooleanField(default=False)

    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)

    def __str__(self):
        return f'{self.id} {self.summary}'

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.save(update_fields=['is_deleted'])
