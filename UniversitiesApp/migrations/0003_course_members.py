# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-08 15:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('UniversitiesApp', '0002_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='members',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]