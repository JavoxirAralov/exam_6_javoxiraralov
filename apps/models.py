from django.db.models import Model, CharField, TextField, ImageField

from django.contrib.auth.models import AbstractUser
from django_resized import ResizedImageField


class User(AbstractUser):
    image = ResizedImageField(size=[200, 200], crop=['middle', 'center'], upload_to='users/images',
                              default='users/default.jpg')


class Product(Model):
    image = ImageField(upload_to='todo_image/', default='todo_image/todo.png')
    title = CharField(max_length=255)
    content = TextField()

    def __str__(self):
        return self.title
