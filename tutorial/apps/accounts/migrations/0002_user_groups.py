# Generated by Django 3.0 on 2020-11-27 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, null=True, to='auth.Group', verbose_name='Permission'),
        ),
    ]
