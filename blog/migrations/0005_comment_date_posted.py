# Generated by Django 3.2 on 2021-04-26 03:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210426_0336'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]