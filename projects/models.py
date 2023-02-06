from django.db import models
from django_quill.fields import QuillField

class Project(models.Model):
    title = models.CharField(max_length=100)
    web_link = models.CharField(max_length=150)
    description = QuillField()
    technology = models.CharField(max_length=150)
    featured_image = models.ImageField(upload_to ='uploads/')

    def __str__(self):
        return self.title
