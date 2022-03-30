# Generated by Django 4.0.3 on 2022-03-30 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url', '0003_alter_url_short_url_alter_url_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='short_url',
            field=models.CharField(blank=True, max_length=1000, unique=True),
        ),
        migrations.AlterField(
            model_name='url',
            name='url',
            field=models.URLField(max_length=1000),
        ),
    ]
