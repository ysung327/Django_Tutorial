# Generated by Django 2.0.7 on 2018-09-01 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0004_auto_20180901_0735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='art',
            name='edition',
            field=models.CharField(max_length=250),
        ),
    ]
