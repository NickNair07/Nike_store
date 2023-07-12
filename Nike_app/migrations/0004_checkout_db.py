# Generated by Django 4.1.7 on 2023-05-16 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nike_app', '0003_cart_db_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout_DB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('mobile', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('district', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]