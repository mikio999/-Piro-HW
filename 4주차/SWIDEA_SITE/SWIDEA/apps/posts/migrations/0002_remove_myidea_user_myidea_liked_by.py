# Generated by Django 4.2.2 on 2023-07-19 05:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myidea',
            name='user',
        ),
        migrations.AddField(
            model_name='myidea',
            name='liked_by',
            field=models.ManyToManyField(blank='True', related_name='liked_ideas', to=settings.AUTH_USER_MODEL, verbose_name='찜한 사용자'),
        ),
    ]
