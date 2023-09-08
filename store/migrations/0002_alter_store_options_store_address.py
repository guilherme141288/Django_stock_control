# Generated by Django 4.2.4 on 2023-08-25 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='store',
            options={'verbose_name': 'Loja', 'verbose_name_plural': 'Lojas'},
        ),
        migrations.AddField(
            model_name='store',
            name='address',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.address', verbose_name='Endereço'),
            preserve_default=False,
        ),
    ]
