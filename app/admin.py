from django.contrib import admin
from .models import Project, Attachment, Comment

admin.site.register(Project)
admin.site.register(Attachment)
admin.site.register(Comment)
