from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    image_profile = models.ImageField(upload_to='profile/image', verbose_name='Фото профиля')
    age = models.IntegerField(verbose_name='Возраст')
    about_me = models.TextField(verbose_name='О себе', blank=True)
    # Внешни ключ
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) :
        return f'{self.first_name} {self.last_name}'

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()