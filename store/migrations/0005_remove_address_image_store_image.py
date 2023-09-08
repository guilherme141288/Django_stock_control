# Generated by Django 4.2.4 on 2023-09-04 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_address_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='image',
        ),
        migrations.AddField(
            model_name='store',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/products/%Y/%m/d'),
        ),
    ]