from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Profile(models.Model):
    name=models.CharField(max_length=50)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    apartment = models.CharField(max_length=50)
    image=models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


    def create_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()



class Products(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=500)
    price = models.IntegerField()
    img_url = models.CharField(max_length=1000, blank=True)

    
    def __str__(self):
        return self.name


class OrderItem(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    t_price = models.IntegerField()

    def __str__(self):
        return self.product.name
