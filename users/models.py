from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
import uuid

from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=200,null=True,blank=True)
    email=models.EmailField(max_length=200,null=True,blank=True)
    username=models.CharField(max_length=200,blank=True,null=True)
    location=models.CharField(max_length=200,blank=True,null=True)
    short_intro=models.CharField(max_length=200,null=True,blank=True)
    bio=models.TextField(blank=True,null=True)
    profile_image=models.ImageField(blank=True,null=True,upload_to='profiles/',default='profiles/user-default.png')
    social_github=models.CharField(max_length=200,null=True,blank=True)
    social_twitter=models.CharField(max_length=200,null=True,blank=True)
    social_linkedin=models.CharField(max_length=200,null=True,blank=True)
    social_youtube=models.CharField(max_length=200,null=True,blank=True)
    social_website=models.CharField(max_length=200,null=True,blank=True)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(editable=False,primary_key=True,default=uuid.uuid4,unique=True)

    def __str__(self):
        return str(self.user.username)

class Skill(models.Model):
    owner=models.ForeignKey(
        Profile,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=200,null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(
        default=uuid.uuid4,primary_key=True,unique=True,editable=False)
    def __str__(self):
        return self.name


def createProfile(sender,instance,created,**kwargs):
    pass


def deleteUser(sender,instance,**kwargs):
    print("Deleting User")


#Using Decorators to make the same thing with the receiver decorator
post_save.connect(createProfile,sender=User)
# post_delete.connect(deleteUser,sender=Profile)