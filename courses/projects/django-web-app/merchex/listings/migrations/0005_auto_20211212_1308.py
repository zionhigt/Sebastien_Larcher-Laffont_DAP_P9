# Generated by Django 3.2.10 on 2021-12-12 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_auto_20211212_1129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='official_homepage',
        ),
        migrations.AlterField(
            model_name='listing',
            name='type',
            field=models.CharField(choices=[('RCD', 'Records'), ('CL', 'Clothing'), ('PO', 'Poster'), ('MIS', 'Miscellaneous')], max_length=5),
        ),
    ]