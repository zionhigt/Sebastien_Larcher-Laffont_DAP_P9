# Generated by Django 3.2.10 on 2022-01-01 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_user_image_profil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image_profil',
            field=models.ImageField(blank=True, help_text='Max: 2mo', null=True, upload_to='images/profils/', verbose_name='Image profil'),
        ),
    ]