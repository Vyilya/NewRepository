from django.urls import path
from .views import *

urlpatterns = [
    path('reguser/', reguserView, name='reguser'),
    path('login/', loginuserview, name='loginuser'),
    path('logout/', logoutuserview, name='logoutuser'),
    path('profile/', profileview, name='profile'),
    path('profileup/', profileupview, name='profileup'),
]
