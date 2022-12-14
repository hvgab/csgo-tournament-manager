# Generated by Django 4.1.3 on 2022-12-02 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_match_clinch_series_match_maplist_match_match_title_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='name',
            new_name='nickname',
        ),
        migrations.AddField(
            model_name='team',
            name='players',
            field=models.ManyToManyField(related_name='teams', to='core.player'),
        ),
    ]
