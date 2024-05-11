# Generated by Django 4.2.11 on 2024-05-08 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='pics')),
                ('des', models.TextField()),
            ],
        ),
    ]
