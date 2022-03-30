from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from users import signals

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, null=True)
    dob =  models.DateField(null=True)
    address = models.CharField(max_length=20, null=True)
    city = models.CharField(max_length=20, null=True)
    country = models.CharField(max_length=20, null=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')


def __str__(self):
    return f'Profile for {self.user.username}'


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

signals.post_save.connect(create_profile, sender=User, weak=False, dispatch_uid='models.create_profile')


# Create your models here.
