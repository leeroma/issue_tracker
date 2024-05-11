from django.db import models


class Status(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Statuses'

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Issue(models.Model):
    summary = models.CharField('Заголовок', max_length=100, null=False, blank=False)
    description = models.CharField('Описание', max_length=3000, null=True, blank=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT, related_name='status', verbose_name='Статус')
    type = models.ForeignKey(Status, on_delete=models.PROTECT, related_name='type', verbose_name='Тип')

    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)

    def __str__(self):
        return self.id, self.summary
