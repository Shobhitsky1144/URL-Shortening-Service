# Generated by Django 3.0.6 on 2020-08-16 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advanceapp', '0004_auto_20200815_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetail',
            name='image',
            field=models.ImageField(null=True, upload_to='profile_pics'),
        ),
    ]
