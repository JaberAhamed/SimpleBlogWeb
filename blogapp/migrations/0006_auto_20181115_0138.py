# Generated by Django 2.1.2 on 2018-11-14 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0005_auto_20181115_0132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articla',
            name='update_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
