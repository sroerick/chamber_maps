# Generated by Django 3.2.8 on 2022-01-26 01:11

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('county', '0015_mapmetadata_toggle_value_display'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapmetadata',
            name='font_color',
            field=colorfield.fields.ColorField(default='#000000', max_length=18, samples=None),
        ),
    ]
