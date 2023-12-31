# Generated by Django 4.2.3 on 2023-07-18 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyDev',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='이름')),
                ('kind', models.CharField(max_length=200, verbose_name='종류')),
                ('content', models.TextField(verbose_name='내용')),
            ],
        ),
        migrations.CreateModel(
            name='MyIdea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=20, verbose_name='유저')),
                ('title', models.CharField(max_length=200, verbose_name='아이디어명')),
                ('image', models.ImageField(blank=True, upload_to='posts/%Y%m%d')),
                ('content', models.TextField(verbose_name='내용')),
                ('interest_rate', models.IntegerField(verbose_name='관심도')),
                ('devtool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', to='posts.mydev', verbose_name='예상 개발툴')),
            ],
        ),
    ]
