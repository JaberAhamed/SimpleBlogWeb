# Generated by Django 2.1.2 on 2018-11-14 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0006_auto_20181115_0138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articla',
            name='update_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
