# Generated by Django 3.0 on 2020-09-01 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20200901_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bdata',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True),
        ),
    ]
