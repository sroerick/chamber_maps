# Generated by Django 3.2.8 on 2022-01-20 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('county', '0008_auto_20220119_2324'),
    ]

    operations = [
        migrations.AddField(
            model_name='mapmetadata',
            name='make_private',
            field=models.BooleanField(default=True),
        ),
    ]
