# Generated by Django 3.1.7 on 2021-04-15 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='track',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='song',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]