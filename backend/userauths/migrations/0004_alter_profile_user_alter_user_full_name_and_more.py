# Generated by Django 4.2.7 on 2024-09-13 05:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0003_user_refresh_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='full_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=100),
        ),
    ]
