# Generated by Django 3.0.6 on 2020-08-15 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advanceapp', '0002_userdetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='mobile',
            field=models.CharField(max_length=10),
        ),
    ]
