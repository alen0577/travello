# Generated by Django 3.2.13 on 2022-04-21 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('img', models.ImageField(upload_to='pictures')),
                ('title', models.CharField(max_length=250)),
                ('cat', models.CharField(max_length=250)),
                ('des', models.TextField()),
            ],
        ),
    ]