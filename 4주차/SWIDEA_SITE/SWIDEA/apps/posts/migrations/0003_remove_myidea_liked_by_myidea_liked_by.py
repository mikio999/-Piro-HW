# Generated by Django 4.2.2 on 2023-07-19 05:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0002_remove_myidea_user_myidea_liked_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myidea',
            name='liked_by',
        ),
        migrations.AddField(
            model_name='myidea',
            name='liked_by',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='liked_idea', to=settings.AUTH_USER_MODEL, verbose_name='찜한 사용자'),
        ),
    ]
