# Generated by Django 3.2.8 on 2022-01-13 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('county', '0006_alter_mapmetadata_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mapmetadata',
            options={'verbose_name': 'Map', 'verbose_name_plural': 'Maps'},
        ),
    ]