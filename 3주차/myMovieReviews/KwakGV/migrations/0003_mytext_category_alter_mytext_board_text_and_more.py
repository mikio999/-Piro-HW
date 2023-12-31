# Generated by Django 4.2.3 on 2023-07-14 05:28

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KwakGV', '0002_mytext_board_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='mytext',
            name='category',
            field=models.CharField(max_length=200, null='True'),
            preserve_default='True',
        ),
        migrations.AlterField(
            model_name='mytext',
            name='board_text',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AlterField(
            model_name='mytext',
            name='genre',
            field=models.CharField(max_length=200, null='True'),
        ),
        migrations.AlterField(
            model_name='mytext',
            name='star_rate',
            field=models.CharField(max_length=200, null='True'),
        ),
        migrations.AlterField(
            model_name='mytext',
            name='year',
            field=models.CharField(max_length=200, null='True'),
        ),
    ]
