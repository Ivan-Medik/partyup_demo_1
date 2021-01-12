from django.urls import path, include
from django.contrib.auth import views

from .views import home, like, login, auth, auth_login, logout, search, search_data


urlpatterns = [

	# Главная страница
	path('', home),
	
	# Выбор языка на главной странице
	path('ru/', home),
	path('en/', home),

	# Страница поиска песен
	path('search/', search),
	path('search/<str:userrequest>', search_data),

	# URL для принятия POST запроса на добавления лайка для песни
	path('like/', like),
	
	# Вход и выход из аккаунт. Авторизация через вк
	path('dev/', auth),
	path('logn/<str:data>', auth_login),
	path('dev/Login', login),
	path('dev/Login/', login),
	path('logout/', logout),

]