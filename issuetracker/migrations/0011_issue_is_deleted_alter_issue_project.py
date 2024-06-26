# Generated by Django 4.2.13 on 2024-05-19 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('issuetracker', '0010_issue_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='issue',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='issues', to='issuetracker.project', verbose_name='Проект'),
        ),
    ]
