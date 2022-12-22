from django.db import models
from djongo import models

# Create your models here.
class Story_Details(models.Model):
    _id = models.ObjectIdField()
    story_title = models.CharField(max_length=500)
    story_level = models.CharField(max_length=10)
    story_image = models.FileField(upload_to='./static/images')
    story_para = models.FileField(upload_to='./static/books')

    def __str__(self):
        return self.story_title