from django.urls import path
from . import views

urlpatterns = [
    path('', views.NewsView, name='News'),
    # http://127.0.0.1:8000/blog/1
    path('<int:article_id>', views.detail, name='detail'),

]
