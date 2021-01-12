from django.db import models
from datetime import date


''' USER '''

class Profile(models.Model):

	first_name = models.CharField(max_length=30, db_index=True)
	last_name = models.CharField(max_length=30, db_index=True)
	identificator = models.CharField(max_length=30, db_index=True)
	socialnetwork = models.CharField(max_length=150, db_index=True)
	socialnetwork_identificator = models.CharField(max_length=30, db_index=True)
	likes = models.CharField(max_length=150, db_index=True)
	downloads = models.CharField(max_length=150, db_index=True)

	def __str__(self):

		return self.socialnetwork + ' - ' + self.first_name + '_' + self.identificator

class Like(models.Model):

	user_identificator = models.CharField(max_length=30, db_index=True)
	song_identificator = models.CharField(max_length=30, db_index=True)

	def __str__(self):

		return self.user_identificator + '_' + self.song_identificator

class Download(models.Model):

	user_identificator = models.CharField(max_length=30, db_index=True)
	song_identificator = models.CharField(max_length=30, db_index=True)

	def __str__(self):

		return self.user_identificator + '_' + self.song_identificator


''' SONGS '''

class TopSong(models.Model):

	identificator = models.CharField(max_length=30, db_index=True)

	def __str__(self):

		return self.identificator


class Song(models.Model):

	name = models.CharField(max_length=30, db_index=True)
	author = models.CharField(max_length=30, db_index=True)
	bpm = models.CharField(max_length=30, db_index=True)
	genre = models.CharField(max_length=30, db_index=True)
	likes = models.CharField(max_length=30, db_index=True)
	version = models.CharField(max_length=30, db_index=True)
	identificator = models.CharField(max_length=30, db_index=True)
	downloads = models.CharField(max_length=30, db_index=True)
	date = models.DateField("Дата загрузки трека", default=date.today)
	audio = models.FileField("Песня", upload_to='audio/')

	def __str__(self):

		return self.name + '_' + self.author + '_' + self.version
