# Generated by Django 4.1.3 on 2022-12-03 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_remove_team_players_alter_team_flag'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='esportal_username',
            field=models.CharField(blank=True, help_text="Hvis dette er linken https://esportal.com/en/profile/Gabbeh/ skal det skrives inn 'Gabbeh' her.", max_length=128, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='steam_id',
            field=models.CharField(blank=True, help_text="SteamId i steamID64 format. (feks '76561197983132487'). Man kan konvertere steam iden sin her https://steamid.io", max_length=128, null=True, unique=True),
        ),
    ]
