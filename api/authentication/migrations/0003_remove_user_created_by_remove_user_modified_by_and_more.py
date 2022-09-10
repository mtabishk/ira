# Generated by Django 4.1 on 2022-09-06 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_staff_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='user',
            name='modified_by',
        ),
        migrations.AlterField(
            model_name='staff',
            name='role',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Guard'), (2, 'Mess Manager'), (3, 'Medical Manager')], default=1),
        ),
    ]