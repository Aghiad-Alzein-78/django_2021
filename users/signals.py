from django.contrib.auth.models import User
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from .models import Profile


# @receiver(signal=post_save,sender=Profile)
def createProfile(sender,instance,created,**kwargs):
    print("Signal createProfile Triggered")
    if created:
        user=instance
        profile=Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name,
        )   
        print("DONE")


# @receiver(signal=post_delete,sender=Profile)    
def deleteUser(sender,instance,**kwargs):
    user=instance.user
    if user!=None:
        user.delete()


#One way of connecting is to use connect function The other way is to use
#the receiver decorator

post_save.connect(createProfile,sender=User)
post_delete.connect(deleteUser,sender=Profile)