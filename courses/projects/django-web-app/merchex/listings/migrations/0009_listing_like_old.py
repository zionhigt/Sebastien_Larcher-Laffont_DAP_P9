# Generated by Django 3.2.10 on 2021-12-12 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0008_auto_20211212_1329'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='like_old',
            field=models.BooleanField(default=False),
        ),
    ]
