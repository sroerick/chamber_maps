# Generated by Django 3.2.8 on 2022-01-13 05:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('county', '0005_auto_20220113_0459'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mapmetadata',
            options={'verbose_name': 'Choropleth Map', 'verbose_name_plural': 'Maps'},
        ),
    ]
