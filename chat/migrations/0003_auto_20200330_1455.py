# Generated by Django 2.2 on 2020-03-30 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_auto_20200330_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='url',
            field=models.CharField(max_length=200),
        ),
    ]
