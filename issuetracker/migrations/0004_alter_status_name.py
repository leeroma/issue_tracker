# Generated by Django 4.2.13 on 2024-05-11 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issuetracker', '0003_alter_issue_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]