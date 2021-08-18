# Generated by Django 3.2.6 on 2021-08-17 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('stack', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('phone_number', models.IntegerField()),
                ('city', models.CharField(default='', max_length=200)),
                ('github', models.URLField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='SkillSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('skills', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='resume.bio')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('course', models.CharField(max_length=200)),
                ('date_from', models.DateField()),
                ('date_to', models.DateField()),
                ('education', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='education', to='resume.bio')),
            ],
        ),
        migrations.CreateModel(
            name='Contact_form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visitor', models.CharField(max_length=200)),
                ('visitor_title', models.CharField(max_length=200)),
                ('visitor_message', models.TextField()),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contact', to='resume.bio')),
            ],
        ),
    ]
