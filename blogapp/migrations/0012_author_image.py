# Generated by Django 2.1.2 on 2018-11-17 11:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0011_auto_20181116_1754'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='image',
            field=models.FileField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
    ]
