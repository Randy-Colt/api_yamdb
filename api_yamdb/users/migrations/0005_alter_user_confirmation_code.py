# Generated by Django 3.2 on 2024-06-12 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_confirmation_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='confirmation_code',
            field=models.CharField(blank=True, editable=False, max_length=20, null=True, unique=True),
        ),
    ]
