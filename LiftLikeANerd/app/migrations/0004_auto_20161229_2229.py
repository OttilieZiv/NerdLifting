# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-29 22:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20161229_1147'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgrammeLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datestamp', models.DateField()),
                ('set_no', models.IntegerField()),
                ('reps', models.IntegerField()),
            ],
            options={
                'db_table': 'programmelog',
            },
        ),
        migrations.CreateModel(
            name='WorkoutDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(blank=True, null=True)),
                ('sets', models.IntegerField()),
                ('reps', models.IntegerField()),
                ('notes', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'workoutdetail',
            },
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='workouts',
        ),
        migrations.AddField(
            model_name='workoutdetail',
            name='exercise',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Exercise'),
        ),
        migrations.AddField(
            model_name='workoutdetail',
            name='workout',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Workout'),
        ),
        migrations.AddField(
            model_name='programmelog',
            name='exercise',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Exercise'),
        ),
        migrations.AddField(
            model_name='programmelog',
            name='programme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Programme'),
        ),
        migrations.AddField(
            model_name='programmelog',
            name='weight',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.WeightConfig'),
        ),
        migrations.AddField(
            model_name='programmelog',
            name='workout',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Workout'),
        ),
    ]
