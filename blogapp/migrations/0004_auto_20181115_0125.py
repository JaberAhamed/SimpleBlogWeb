# Generated by Django 2.1.2 on 2018-11-14 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_articla_update_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articla',
            name='posted_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
