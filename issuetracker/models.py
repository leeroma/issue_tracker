from django.db import models

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


class Issue(models.Model):
    summary = models.CharField('Заголовок', max_length=100, null=False, blank=False,
                               validators=[validate_language, check_len, ])
    description = models.TextField('Описание', max_length=3000, null=True, blank=True, validators=[validate_language, ])
    status = models.ForeignKey(Status, on_delete=models.PROTECT, related_name='status', verbose_name='Статус')
    type = models.ForeignKey(Type, on_delete=models.PROTECT, related_name='type', verbose_name='Тип')

    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)

    def __str__(self):
        return f'{self.id} {self.summary}'
