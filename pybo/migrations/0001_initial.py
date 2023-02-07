# Generated by Django 3.1.3 on 2023-02-07 03:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('create_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Thema',
            fields=[
                ('t_no', models.IntegerField(primary_key=True, serialize=False)),
                ('t_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Path',
            fields=[
                ('p_no', models.IntegerField(primary_key=True, serialize=False)),
                ('p_name', models.CharField(max_length=20)),
                ('detail', models.TextField()),
                ('distance', models.CharField(max_length=10)),
                ('time', models.CharField(max_length=10)),
                ('th_no', models.ForeignKey(db_column='t_no', on_delete=django.db.models.deletion.CASCADE, to='pybo.thema')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('create_date', models.DateTimeField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pybo.question')),
            ],
        ),
    ]
