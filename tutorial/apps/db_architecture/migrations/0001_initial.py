# Generated by Django 3.0 on 2020-11-05 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='UserPersonalInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=64)),
                ('gender', models.CharField(choices=[('male', 'Erkak'), ('female', 'Ayol')], default='male', max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='UserServiceEvaluationRank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db_architecture.Service')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db_architecture.UserPersonalInfo')),
            ],
        ),
        migrations.AddField(
            model_name='userpersonalinfo',
            name='services',
            field=models.ManyToManyField(through='db_architecture.UserServiceEvaluationRank', to='db_architecture.Service'),
        ),
    ]
