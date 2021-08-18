# Generated by Django 3.2.6 on 2021-08-17 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact_form',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='school',
            name='education',
        ),
        migrations.RemoveField(
            model_name='skillset',
            name='skills',
        ),
        migrations.AddField(
            model_name='contact_form',
            name='visitor_email',
            field=models.EmailField(default='', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skillset',
            name='level',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
