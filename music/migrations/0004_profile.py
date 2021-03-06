# Generated by Django 3.1.3 on 2020-12-27 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_song'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(db_index=True, max_length=30)),
                ('last_name', models.CharField(db_index=True, max_length=30)),
                ('identificator', models.CharField(db_index=True, max_length=30)),
                ('socialnetwork', models.CharField(db_index=True, max_length=150)),
                ('socialnetwork_identificator', models.CharField(db_index=True, max_length=30)),
                ('likes', models.CharField(db_index=True, max_length=150)),
                ('downloads', models.CharField(db_index=True, max_length=150)),
                ('subscribers', models.CharField(db_index=True, max_length=10)),
                ('posts', models.CharField(db_index=True, max_length=10)),
                ('saveds', models.CharField(db_index=True, max_length=10)),
                ('markeds', models.CharField(db_index=True, max_length=10)),
            ],
        ),
    ]
