# Generated by Django 3.1.3 on 2023-02-08 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tema', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Path',
            fields=[
                ('p_no', models.IntegerField(primary_key=True, serialize=False)),
                ('p_name', models.CharField(max_length=20)),
                ('detail', models.TextField()),
                ('distance', models.CharField(max_length=10)),
                ('time', models.CharField(max_length=10)),
                ('th_no', models.ForeignKey(db_column='t_no', on_delete=django.db.models.deletion.CASCADE, to='tema.thema')),
            ],
        ),
    ]
