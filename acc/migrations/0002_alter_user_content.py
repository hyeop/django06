# Generated by Django 4.0.5 on 2022-06-19 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='content',
            field=models.TextField(blank=True),
        ),
    ]
