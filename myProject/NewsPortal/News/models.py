from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField('Название категории', max_length=50)
class Article(models.Model):
    title = models.CharField('Заголовок', max_length=50)
    desc = models.TextField('Описание')
    image = models.ImageField('Изображение', upload_to='News/image/')
    date = models.DateField('Дата')
    url = models.URLField('Доп. источник', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return f"{self.title} | {self.date} "