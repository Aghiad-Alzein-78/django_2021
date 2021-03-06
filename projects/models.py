from django.db import models
import uuid

from django.db.models.deletion import SET_NULL
from users.models import Profile

# Create your models here.
class Project(models.Model):
    owner=models.ForeignKey(Profile,null=True,blank=True,on_delete=SET_NULL)
    title=models.CharField(max_length=200)
    description=models.TextField(null=True,blank=True)
    demo_link=models.CharField(max_length=2000,null=True,blank=True)
    source_link=models.CharField(max_length=2000,null=True,blank=True)
    featured_image=models.ImageField(null=True,blank=True,default='default.jpg')
    tags=models.ManyToManyField('Tag',blank=True)
    votes_total=models.IntegerField(default=0,null=True,blank=True)
    votes_ratio=models.IntegerField(default=0,null=True,blank=True)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,primary_key=True,unique=True,editable=False)
    
    def __str__(self):
        return self.title

    # will return the results of a project always in date of created
    #if we change created to be ["-created"]
    class Meta:
        ordering=['-votes_ratio','-votes_total','title']

    @property
    def reviewers(self):
       return self.review_set.all().values_list("owner__id",flat=True)

    @property
    def getVoteCount(self):
        reviews=self.review_set.all()
        upVotes=reviews.filter(value="up").count()
        totalVotes=reviews.count()
        ratio=int(upVotes/totalVotes*100)
        self.votes_total=totalVotes
        self.votes_ratio=ratio
        self.save()




class Review(models.Model):
    VOTE_TYPE=(
        ('up','Up Vote'),
        ('down','Down Vote')
    )
    owner=models.ForeignKey(Profile,null=True,blank=True,on_delete=models.CASCADE)
    project=models.ForeignKey(Project,on_delete=models.CASCADE)
    body=models.TextField(null=True,blank=True)
    value=models.CharField(max_length=200,choices=VOTE_TYPE)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,primary_key=True,unique=True,editable=False)
    
    class Meta:
        unique_together=[['owner','project']]

    def __str__(self):
        return self.value
    

class Tag(models.Model):
    name=models.CharField(max_length=100)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,primary_key=True,unique=True,editable=False)

    def __str__(self):
        return self.name