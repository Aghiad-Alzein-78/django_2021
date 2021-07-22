from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
import uuid
# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=200,null=True,blank=True)
    email=models.EmailField(max_length=200,null=True,blank=True)
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