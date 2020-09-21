# Generated by Django 3.0.8 on 2020-09-17 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avto', '0005_equipment_capacity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='gearbox',
            field=models.CharField(choices=[('Manual', ' Механическая'), ('Automatic', 'Автоматическая'), ('Robotic', 'Робот')], default='Automatic', max_length=15, verbose_name='Коробка передач'),
        ),
    ]
