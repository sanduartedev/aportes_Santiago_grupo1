# Generated by Django 3.2.14 on 2022-11-20 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turnos', '0006_alter_proyecto_portada'),
    ]

    operations = [
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('nombre_slug', models.SlugField(max_length=100, verbose_name='Nombre Slug')),
                ('anio', models.IntegerField(verbose_name='Año')),
                ('cargo', models.TextField(null=True, verbose_name='Descripcion')),
                ('foto', models.ImageField(null=True, upload_to='static/img/', verbose_name='Portada')),
            ],
        ),
        migrations.DeleteModel(
            name='Proyecto',
        ),
    ]
