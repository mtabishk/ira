# Generated by Django 4.0.4 on 2022-08-20 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30)),
                ('designation', models.CharField(default='', max_length=30)),
                ('profile', models.CharField(max_length=100)),
                ('linkedIn_url', models.URLField()),
                ('github_url', models.URLField()),
            ],
        ),
    ]
