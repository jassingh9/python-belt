# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-25 18:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.DateField(),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='friend',
            name='client_friend',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend_sender', to='friends.User'),
        ),
        migrations.AddField(
            model_name='friend',
            name='receive_friend',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend_receiver', to='friends.User'),
        ),
    ]
