# Generated by Django 2.1.2 on 2018-11-14 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_articla_posted_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='articla',
            name='update_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
