# Generated by Django 3.2.14 on 2022-11-21 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turnos', '0008_auto_20221120_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal',
            name='cargo',
            field=models.TextField(null=True, verbose_name='Cargo'),
        ),
        migrations.AlterField(
            model_name='personal',
            name='foto',
            field=models.ImageField(null=True, upload_to='media', verbose_name='Foto'),
        ),
    ]
