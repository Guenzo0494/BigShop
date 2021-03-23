from django.db import models

from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from autoslug import  AutoSlugField

# Create your models here.

#Category model
class Category(models.Model):
    title = models.CharField(max_length=300, blank=False, unique=True)
    primaryCategory = models.BooleanField(default=False)

    def __str__(self):
        return self.title


#Product Model
class  Product(models.Model):
    mainimage = models.ImageField(upload_to='products/', blank=False)
    name = models.CharField(max_length=300)
    slug = AutoSlugField(populate_from='name', unique_with=('id', 'price'))
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    detail_text = models.TextField(max_length=1000, verbose_name='Detail Text')
    price = models.FloatField()
    

    def __str__(self):
        return self.name



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.user.first_name

    # @receiver(post_save, sender=User)
    # def create_user_profile(self, sender, instance, created, **kwargs):
    #     if created:
    #         Profile.objects.create(user=instance)

    # @receiver(post_save, sender=User)
    # def save_user_profile(self, sender, instance, **kwargs):
    #     instance.profile.save()
