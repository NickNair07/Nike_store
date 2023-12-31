# Generated by Django 4.1.7 on 2023-04-02 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(blank=True, max_length=255, null=True)),
                ('p_name', models.CharField(blank=True, max_length=255, null=True)),
                ('p_qty', models.IntegerField(blank=True, null=True)),
                ('p_price', models.IntegerField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('p_image', models.ImageField(upload_to='product_images')),
            ],
        ),
    ]
