# Generated by Django 2.1.5 on 2019-04-21 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beneficiary', '0002_auto_20190421_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fund',
            name='balance',
            field=models.BigIntegerField(),
        ),
    ]
