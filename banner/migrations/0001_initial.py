# Generated by Django 5.1 on 2024-08-14 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner_1', models.ImageField(blank=True, null=True, upload_to='banners/')),
                ('banner_2', models.ImageField(blank=True, null=True, upload_to='banners/')),
                ('banner_3', models.ImageField(blank=True, null=True, upload_to='banners/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]