# Generated by Django 2.0.1 on 2018-02-01 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClimateModel',
            fields=[
                ('model_name', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Experiment',
            fields=[
                ('experiment_name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PerformanceMonitoring.ClimateModel')),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_name', models.CharField(max_length=50, unique=True)),
                ('user_name', models.CharField(max_length=50)),
                ('repository', models.CharField(max_length=256)),
                ('revision', models.CharField(max_length=40)),
                ('branch', models.CharField(max_length=64)),
                ('submitted', models.DateTimeField()),
                ('start_date', models.DateTimeField()),
                ('stop_date', models.DateTimeField()),
                ('n_mpi_ranks', models.SmallIntegerField()),
                ('n_omp_threads', models.SmallIntegerField()),
                ('simulated_time', models.DurationField()),
                ('experiment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PerformanceMonitoring.Experiment')),
            ],
        ),
    ]
