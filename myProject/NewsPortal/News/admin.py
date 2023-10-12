from django.contrib import admin
from .models import Article, Category


admin.site.register(Category)
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','date')

