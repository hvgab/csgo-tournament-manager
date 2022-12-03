# Generated by Django 4.1.3 on 2022-11-28 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_gameserver_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='series_type',
            field=models.CharField(choices=[('MAP PRESET', (('BO1_MAP_PRESET', 'BO1 with map preset'),)), ('MAP VETO', (('BO1_MAP_VETO', 'BO1 with map veto'), ('BO3_MAP_VETO', 'BO3 with map veto')))], default='BO3_MAP_VETO', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='player1',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='player2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='player3',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='player4',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='player5',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='player6',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='player7',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='api_key',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='cancelled',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='forfeit',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='max_maps',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='plugin_version',
            field=models.CharField(blank=True, default='unknown', max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='skip_veto',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='team1_score',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='team2_score',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='title',
            field=models.CharField(blank=True, default='', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='veto_mappool',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='winner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='match_set_as_team_winner', to='core.team'),
        ),
    ]
