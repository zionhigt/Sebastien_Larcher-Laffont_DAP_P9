# Generated by Django 3.2.10 on 2021-12-12 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0007_band_like_new'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='band',
            name='like_new',
        ),
        migrations.AddField(
            model_name='listing',
            name='like_new',
            field=models.BooleanField(default=False),
        ),
    ]
