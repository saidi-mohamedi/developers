# Generated by Django 4.1.4 on 2023-01-20 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoApp', '0003_project_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-created']},
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(max_length=200),
        ),
    ]
