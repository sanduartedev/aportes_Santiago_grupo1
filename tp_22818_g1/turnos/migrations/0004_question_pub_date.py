# Generated by Django 3.2.14 on 2022-11-20 17:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('turnos', '0003_remove_question_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 20, 17, 40, 16, 908658, tzinfo=utc), verbose_name='date_published'),
            preserve_default=False,
        ),
    ]
