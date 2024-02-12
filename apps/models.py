
from django.contrib.auth.models import AbstractUser
from django.db.models import Model, CharField, ImageField, PositiveIntegerField, FloatField, DateTimeField
from django_ckeditor_5.fields import CKEditor5Field
from django_resized import ResizedImageField


class User(AbstractUser):
    image = ResizedImageField(size=[200, 200], crop=['middle', 'center'], upload_to='users/images',
                              default='users/default.jpg')


class Product(Model):
    title = CharField(max_length=255)
    image = ImageField(upload_to='product/images', default='product/default.jpg')
    description = CKEditor5Field(blank=True, null=True)
    quantity = PositiveIntegerField(default=0)
    price = FloatField()
    updated_at = DateTimeField(auto_now=True)
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

