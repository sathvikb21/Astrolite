# Generated by Django 4.1.7 on 2023-03-27 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_userdetail_total_trips'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetail',
            name='total_orders',
            field=models.IntegerField(default=0),
        ),
    ]
