# Generated by Django 2.1 on 2018-08-24 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Art',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('art_title', models.CharField(max_length=500)),
                ('theme', models.CharField(max_length=250)),
                ('preview', models.FileField(upload_to='')),
                ('size1', models.CharField(max_length=100)),
                ('size2', models.IntegerField()),
                ('size3', models.CharField(max_length=100)),
                ('media', models.CharField(max_length=250)),
                ('frame', models.CharField(max_length=250)),
                ('edition', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist_name', models.CharField(max_length=250)),
                ('artist_photo', models.FileField(upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='art',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rental.Artist'),
        ),
    ]
