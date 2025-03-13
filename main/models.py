from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

import os

# Create your models here.

class CustomUser(AbstractUser):
    birth_date = models.DateField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='users/', blank=True, null=True)

    groups = models.ManyToManyField(
        Group,
        related_name="customuser_set",
        blank=True
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_permissions_set",
        blank=True
    )



class Article(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(upload_to='articles')
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.SmallIntegerField()
    update = models.DateTimeField(auto_now=True)


    def delete(self, *args, **kwargs):  # Rasmni o'chirish
        if self.image and os.path.isfile(self.image.path):
            os.remove(self.image.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.title



class View(models.Model): # ko'rishlar uchun model prosmotrlar articlar ni
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    custom_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return "Ko'rilgan" if self.custom_user else None



class Team(models.Model):
    full_name = models.CharField(max_length=70)
    birth_date = models.DateField()
    image = models.ImageField(upload_to='teams')
    address = models.CharField(max_length=70)
    position = models.CharField(max_length=30)
    description = models.TextField()
    instagram = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)

    def delete(self, *args, **kwargs):  # Rasmni o'chirish
        if self.image and os.path.isfile(self.image.path):
            os.remove(self.image.path)
        super().delete(*args, **kwargs)


    def __str__(self):
        return self.full_name





