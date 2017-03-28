from __future__ import unicode_literals
from django.db import models

# Create your models here.
class CourseManager(models.Manager):
    def addClass(self, data):
        if len(data['name']) == 0 or len(data['description'])==0:
            return (False, "Please enter a value in Name and Description Fields")
        else:
            valid_name= Course.objects.create(name=data['name'], description = data['description'])
            return(True, valid_name)


class Course(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CourseManager()
