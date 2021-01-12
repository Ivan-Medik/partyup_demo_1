# Generated by Django 3.1.3 on 2020-12-27 20:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0005_download_like'),
    ]

    operations = [
        migrations.RenameField(
            model_name='download',
            old_name='like_post_creator',
            new_name='song_identificator',
        ),
        migrations.RenameField(
            model_name='download',
            old_name='like_post_identificator',
            new_name='user_identificator',
        ),
        migrations.RemoveField(
            model_name='download',
            name='like_user_identificator',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='markeds',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='posts',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='saveds',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='subscribers',
        ),
    ]