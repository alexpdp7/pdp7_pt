# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-25 19:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Measure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('when', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('measure_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='DoublePositiveIntegerMeasure',
            fields=[
                ('measure_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='measures.Measure')),
                ('value_1', models.PositiveIntegerField()),
                ('value_2', models.PositiveIntegerField()),
            ],
            bases=('measures.measure',),
        ),
        migrations.CreateModel(
            name='FloatMeasure',
            fields=[
                ('measure_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='measures.Measure')),
                ('value', models.FloatField()),
            ],
            bases=('measures.measure',),
        ),
        migrations.AddField(
            model_name='measure',
            name='series',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='measures.Series'),
        ),
        migrations.AddField(
            model_name='measure',
            name='who',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]