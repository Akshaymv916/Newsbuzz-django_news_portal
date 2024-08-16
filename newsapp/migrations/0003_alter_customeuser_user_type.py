# Generated by Django 5.1 on 2024-08-14 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0002_alter_customeuser_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeuser',
            name='user_type',
            field=models.CharField(choices=[(2, 'subadmin'), (1, 'admin')], default=1, max_length=100),
        ),
    ]
