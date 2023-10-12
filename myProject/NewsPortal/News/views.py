from django.shortcuts import render, get_object_or_404

from .models import Article, Category # подключение базы данных
app_name = 'News'
def NewsView(request):
    articles = Article.objects.all() # отвечает за хранение подключенной базы

    return render(request, template_name='News/News.html', context={'articles': articles})

def detail(request, article_id):
    article = get_object_or_404(Article, pk = article_id)
    return render(request, 'detail/detail.html', {'article':article})