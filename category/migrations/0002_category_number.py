# Generated by Django 3.0.2 on 2020-02-01 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='number',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]