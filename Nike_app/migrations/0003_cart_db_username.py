# Generated by Django 4.1.7 on 2023-05-12 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nike_app', '0002_cart_db'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart_db',
            name='username',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
