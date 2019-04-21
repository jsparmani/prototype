# Generated by Django 2.1.5 on 2019-04-21 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beneficiary', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fund',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.PositiveIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='beneficiary',
            name='account_number',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='beneficiary',
            name='ifsc_code',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]