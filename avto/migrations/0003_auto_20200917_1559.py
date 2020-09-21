# Generated by Django 3.0.8 on 2020-09-17 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('avto', '0002_auto_20200917_1512'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brend',
            options={'verbose_name': 'Марка', 'verbose_name_plural': 'Марки'},
        ),
        migrations.AlterModelOptions(
            name='characteristic',
            options={'verbose_name': 'Характеристики', 'verbose_name_plural': 'Характеристики'},
        ),
        migrations.AlterModelOptions(
            name='generation',
            options={'verbose_name': 'Поколение', 'verbose_name_plural': 'Поколения'},
        ),
        migrations.AlterModelOptions(
            name='model',
            options={'verbose_name': 'Модель', 'verbose_name_plural': 'Модели'},
        ),
        migrations.AlterModelOptions(
            name='modelimage',
            options={'verbose_name': 'Изображение', 'verbose_name_plural': 'Изображения'},
        ),
        migrations.RemoveField(
            model_name='characteristic',
            name='models',
        ),
        migrations.AddField(
            model_name='characteristic',
            name='generations',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Characteristic', to='avto.Generation'),
            preserve_default=False,
        ),
    ]
