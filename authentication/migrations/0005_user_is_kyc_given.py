# Generated by Django 5.1 on 2024-10-08 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_managekyc'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_kyc_given',
            field=models.BooleanField(default=True, null=True),
        ),
    ]
