# Generated by Django 4.1.3 on 2022-11-08 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_gameserver_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameserver',
            name='ssh_password',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='gameserver',
            name='ssh_user',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
