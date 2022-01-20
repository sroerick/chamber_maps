# Generated by Django 3.2.8 on 2022-01-13 04:59

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('county', '0004_alter_mapgeometry_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='stateTiger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=2)),
                ('division', models.CharField(max_length=2)),
                ('statefp', models.CharField(max_length=2)),
                ('statens', models.CharField(max_length=8)),
                ('geoid', models.CharField(max_length=2)),
                ('stusps', models.CharField(max_length=2)),
                ('name', models.CharField(max_length=100)),
                ('lsad', models.CharField(max_length=2)),
                ('mtfcc', models.CharField(max_length=5)),
                ('funcstat', models.CharField(max_length=1)),
                ('aland', models.BigIntegerField()),
                ('awater', models.BigIntegerField()),
                ('intptlat', models.CharField(max_length=11)),
                ('intptlon', models.CharField(max_length=12)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.AlterModelOptions(
            name='mapmetadata',
            options={'verbose_name': 'Map', 'verbose_name_plural': 'Maps'},
        ),
    ]
