# Generated by Django 3.2.6 on 2021-08-18 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_auto_20210817_1656'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact_form',
            name='title',
        ),
        migrations.AlterField(
            model_name='contact_form',
            name='message',
            field=models.TextField(),
        ),
    ]
