# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cdate', models.DateField()),
                ('cbody', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mtitle', models.CharField(max_length=50)),
                ('mbody', models.TextField(max_length=5000)),
                ('mdate', models.DateField()),
                ('mread', models.IntegerField(default=0)),
                ('mlike', models.IntegerField(default=0)),
                ('mshare', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Usr',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uname', models.CharField(max_length=20)),
                ('upassword', models.CharField(max_length=20)),
                ('ustate', models.CharField(max_length=50)),
                ('ugender', models.BooleanField()),
                ('ulogo', models.IntegerField()),
                ('ubackground', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='mowner',
            field=models.ForeignKey(to='blog.Usr'),
        ),
        migrations.AddField(
            model_name='comt',
            name='cowner',
            field=models.ForeignKey(to='blog.Usr'),
        ),
    ]
