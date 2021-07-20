from django.db import models
import uuid
# Create your models here.
class Project(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField(null=True,blank=True)
    demo_link=models.CharField(max_length=2000,null=True,blank=True)
    source_link=models.CharField(max_length=2000,null=True,blank=True)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,primary_key=True,unique=True,editable=False)
    
    def __str__(self):
        return self.title

class Reviews(models.Model):
    # owner
    # project
    body=models.TextField(null=True,blank=null)