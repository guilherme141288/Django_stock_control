# Generated by Django 4.2.4 on 2023-09-04 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_remove_address_image_store_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='city',
            field=models.CharField(max_length=100, null=True, verbose_name='Cidade'),
        ),
        migrations.AddField(
            model_name='store',
            name='state',
            field=models.CharField(max_length=20, null=True, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='store',
            name='address',
            field=models.CharField(max_length=100, null=True, verbose_name='Rua'),
        ),
        migrations.AlterField(
            model_name='store',
            name='date_of_fundation',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/products/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='store',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Nome'),
        ),
        migrations.DeleteModel(
            name='Address',
        ),
    ]
