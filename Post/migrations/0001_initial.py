# Generated by Django 3.0.5 on 2020-04-03 22:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now_add=True)),
                ('slug', models.SlugField(unique=True)),
                ('auteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.Profile')),
            ],
        ),
    ]