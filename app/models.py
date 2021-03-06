from django.db import models
from datetime import datetime
from django.utils import timezone

class Project(models.Model):
    name = models.CharField(max_length=100, default="")
    description = models.TextField(max_length=1000, default="")
    owner = models.CharField(max_length=100, default="")
    startdate = models.DateTimeField(default=timezone.now)
    language = models.CharField(max_length=100, default="")
    status = models.CharField(max_length=100, default="")
    finished = models.BooleanField(default=False)
    finishdate = models.DateTimeField(default=timezone.now)
    archived = models.BooleanField(default=False)
    archivedate = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name

class Attachment(models.Model):    
    name = models.CharField(max_length=100, default="")
    file = models.FileField(upload_to="attachments/", blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_attachment', default=None)

    def __str__(self):
        return self.name

class Comment(models.Model):    
    name = models.CharField(max_length=100, default="")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_comment', default=None)
    comment = models.TextField(max_length=1000, default="")
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name