# Generated by Django 3.0.5 on 2020-04-03 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
