# Generated by Django 4.2.13 on 2024-05-18 11:10

from django.db import migrations, models
import issuetracker.form_validators


class Migration(migrations.Migration):

    dependencies = [
        ('issuetracker', '0007_alter_issue_description_alter_issue_summary'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, validators=[issuetracker.form_validators.validate_language], verbose_name='Название')),
                ('description', models.TextField(blank=True, max_length=3000, null=True, validators=[issuetracker.form_validators.validate_language], verbose_name='Описание')),
                ('start', models.DateField(verbose_name='Дата начала')),
                ('deadline', models.DateField(blank=True, verbose_name='Дата окончания')),
            ],
        ),
    ]
