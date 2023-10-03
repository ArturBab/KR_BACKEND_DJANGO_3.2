from collections.abc import Iterable
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.files.storage import default_storage
from django.utils import timezone

class File(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='files/')

    def save(self, *args, **kwargs):
        # Сохраняем файл в хранилище MinIO
        self.file.name = f"files/{timezone.now().strftime('%Y-%m-%d_%H-%M-%S')}_{self.file.name}"
        super().save(*args, **kwargs)

class User(AbstractUser):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    REQUIRED_FIELDS = []


class Author(models.Model):
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    surname = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'id = {self.id}, first_name = {self.first_name}, last_name = {self.last_name}, surname = {self.surname}'


class Article(models.Model):
    name_article = models.CharField(max_length=255, blank=True, null=True)
    author = models.ForeignKey('Author', on_delete=models.PROTECT, null=True)
    appeal = models.CharField(max_length=255, blank=True, null=True)
    notification = models.CharField(max_length=255, blank=True, null=True)
    year_of_publication = models.DateField(blank=True, null=True)
    theme = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    url_article = models.CharField(max_length=255, blank=True, null=True)
    url_permission = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(User, verbose_name='User',
                             on_delete=models.CASCADE)

    def __str__(self):
        return f'id = {self.id}, name_article = {self.name_article}, author = {self.author}'
# Create your models here.
