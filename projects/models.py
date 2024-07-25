from django.db import models
import uuid

class Project(models.Model):
    title = models.CharField(max_length=200) 
    description = models.TextField(null=True, blank=True)
    demo_link = models.CharField(max_length=2000,null=True, blank=True)
    source_link = models.CharField(max_length=2000,null=True, blank=True)
    # if Tag class it ubove you can Tag with out quotation but it blew you need to add quotation
    tags = models.ManyToManyField('Tag', blank=True)
    # vote_total means total votes for this project and default is 0 
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    # vote_ratio means total votes for this project divided by total votes for all projects , its percentage
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default =uuid.uuid4, unique=True, primary_key=True, editable=False)
    # when i create a new project it does't show the title of the project you can use this method
    def __str__(self):
        return self.title

class Review(models.Model):
    # VOTE_TYPE for upvote and downvote
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote')
    )
    # owner =
    # this is mean if you delete the project it will delete the review you call the project in parameter
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    #  choices=VOTE_TYPE for upvote and downvote
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default =uuid.uuid4, unique=True, primary_key=True, editable=False)

    # class Meta:
    #     unique_together = [['owner', 'project']]
     # return self.value means it will return up or down votes for the project
    def __str__(self):
        return self.value
# this is tag class for you to add react and 
class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default =uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name
