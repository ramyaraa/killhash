from django.db import models
import uuid

class project(models.Model):
    #create a title for the project and maximum number of title is 200 characters
    title = models.CharField(max_length=200) 
    #create a description for the project , null=True means that the description is empty or you can write charecters
    # and blank=True means same , but null=True for table to know , blank=True for django to know 
    description = models.TextField(null=True, blank=True)
    #create a demo link for the project and maximum number of demo link is 2000 characters
    demo_link = models.CharField(max_length=2000,null=True, blank=True)
    source_link = models.CharField(max_length=2000,null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    #create a id for each project and it will be unique and not editable and primary key will be uuid for each project
    id = models.UUIDField(default =uuid.uuid4, unique=True, primary_key=True, editable=False)