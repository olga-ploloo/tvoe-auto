# Generated by Django 3.0.8 on 2020-09-17 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avto', '0004_auto_20200917_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='capacity',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Мощность'),
        ),
    ]
