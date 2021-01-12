from django.contrib.auth.models import User as Users
from django.views.generic import CreateView
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login as loginUser, logout as logoutUser
from .forms import UserRegistrationForm
from django.shortcuts import redirect
from django.http import HttpResponse
from django.shortcuts import render

from .forms import *
from .models import *

import requests
import json



def home(request):

	isuser = request.user.is_authenticated

	songs = Song.objects.all()
	likes = Like.objects.filter(user_identificator=request.user.id)

	songs_likes = []


	for song in songs:

		try:

			islike = Like.objects.filter(song_identificator=song.identificator)[0]
			songs_likes.append(islike.song_identificator)

		except Exception:

			pass


	topsongs = TopSong.objects.all()

	topsongs_new = []

	for topsong in topsongs:

		topsong_new = Song.objects.filter(identificator=topsong.identificator)

		topsongs_new.append(topsong_new[0])


	if request.path == '/en/':

		en = True
		ru = False

	elif request.path == '/ru/':

		ru = True
		en = False

	else:

		ru = False
		en = False

	try:
		
		profile = Profile.objects.filter(identificator=request.user.id)[0]

	except Exception:

		profile = None

	print('\n\n\n')
	print('songs_likes -', songs_likes)
	print('\n\n\n')

	context = {

		"Songs": songs,
		"songs_likes": songs_likes,
		"TopSongs": topsongs_new,
		"profile": profile,
		"isUser": isuser,
		"ru": ru,
		"en": en,

	}

	return render(request, 'music/home.html', context=context)


def like(request):

	if request.user.is_authenticated:

		form_data = json.loads(request.body)

		if form_data[1] == True:

			likes = Like.objects.filter(user_identificator = request.user.id, song_identificator=form_data[0])

			try:

				like = likes[0]

			except Exception:

				like = None

			if like != None:

				like.delete()

				song = Song.objects.filter(identificator=form_data[0])[0]

				song.likes = str(int(song.likes) - 1)

				song.save()


			return HttpResponse()

		else:

			# Проверяю, не создан ли уже случайно такой лайк =)
			likes = Like.objects.filter(user_identificator = request.user.id, song_identificator=form_data[0])

			try:

				like = likes[0]

			except Exception:

				like = None

			if like == None:

				like = Like()
				like.user_identificator = request.user.id
				like.song_identificator = form_data[0]
				like.save()

				song = Song.objects.filter(identificator=form_data[0])[0]

				song.likes = str(int(song.likes) + 1)

				song.save()


			return HttpResponse()

	return redirect('/')




def search(request):

	context = {

	}


	return render(request, 'music/search.html', context=context)


def search_data(request, userrequest):

	context = {

	}


	return render(request, 'music/search.html', context=context)





''' Вход и выход из аккаунта '''

def login(request):

	print(request.GET)

	check = True

	try:

		user = Users.objects.filter(username = request.GET['first_name'], email = request.GET['uid'])[0]
		check = False

	except Exception:

		pass

	if check:

		context = {

			"uid":request.GET['uid'],
			"first_name":request.GET['first_name'],
			"last_name":request.GET['last_name'],

		}

		user = User.objects.create_user(request.GET['first_name'], request.GET['uid'], request.GET['uid'])
		user.first_name = request.GET['first_name']
		user.last_name = request.GET['last_name']
		user.save()

		profile = Profile()
		profile.first_name = request.GET['first_name']
		profile.last_name = request.GET['last_name']
		profile.identificator = user.id
		profile.socialnetwork = 'vk'
		profile.socialnetwork_identificator = request.GET['uid']
		profile.likes = 0
		profile.downloads = 0

		profile.save()




	username = request.GET['first_name']
	password = request.GET['uid']
	user = authenticate(request, username=username, password=password)

	if user is not None:

		loginUser(request, user)

		return redirect('/')

		# return render(request, 'registration/login.html', context=context)

def logout(request):

	logoutUser(request)

	return redirect('/')

def auth(request):

	if request.method == 'POST':

		print('\n\n\n')
		print(request.POST)
		print('\n\n\n')
		check = True

		try:

			user = Users.objects.filter(username = request.POST['username'], email = request.POST['password'])[0]
			check = False

		except Exception:

			pass

		if check:

			user_form = UserRegistrationForm(request.POST)
			if user_form.is_valid():
				# Create a new user object but avoid saving it yet
				new_user = user_form.save(commit=False)
				# Set the chosen password
				new_user.set_password(user_form.cleaned_data['password'])
				# Save the User object
				new_user.save()

				new_user.first_name = request.POST['username']
				new_user.last_name = request.POST['first_name']
				new_user.email = request.POST['password']

				new_user.save()
				
				user = Users.objects.filter(username = new_user, email = new_user.email)[0]


def auth_login(request, data):

	print('\n\n\n')
	print(':' + str(data) + ':')
	print('\n\n\n')

	data = data.split('&')


	user = authenticate(request, username=data[1], password=data[0])

	if user is not None:

		login(request, user)

	else:

		print('\n\n\n')
		print(':LLLLLLLLLLLLLLLLLLLLLLLLLL:')
		print('\n\n\n')


	return redirect('/')
