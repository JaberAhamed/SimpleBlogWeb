# Generated by Django 2.1.2 on 2018-11-16 11:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0010_articla_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articla',
            name='image',
            field=models.FileField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
    ]
