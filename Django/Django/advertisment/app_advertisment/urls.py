from django.urls import path
from .views import index, top_sellers, register, profile, login, advertisement, advertisement_post

urlpatterns=[
    path('', index, name='main page'),
    path('top-sellers/', top_sellers, name='top sellers page'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('login/', login, name='login'),
    path('advertisement/', advertisement, name='advertisement'),
    path('advertisement_post/',advertisement_post, name='advertisement_post')
]