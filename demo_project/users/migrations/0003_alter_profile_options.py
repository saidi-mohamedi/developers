# Generated by Django 4.1.4 on 2023-01-25 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_profile_image_skill'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['-created']},
        ),
    ]
