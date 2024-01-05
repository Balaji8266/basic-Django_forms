# Generated by Django 4.2.6 on 2024-01-05 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('deptno', models.IntegerField(primary_key=True, serialize=False)),
                ('dname', models.CharField(max_length=100)),
                ('dloc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('eid', models.IntegerField(primary_key=True, serialize=False)),
                ('ename', models.CharField(max_length=100)),
                ('sal', models.IntegerField()),
                ('deptno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.dept')),
            ],
        ),
    ]