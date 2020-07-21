from django.db import models
from datetime import *

# Create your models here.
class ShowManager(models.Manager):
    def showValidator(self, postData):
        error = {}
        if len(postData['title']) < 2:
            error['title'] = "You must include a title at least 2 characters long."
        show = Show.objects.filter(title=postData['title'])
        if show:
            error['title'] = "That show is already listed."
        if len(postData['network']) < 3:
            error['network'] = "You must include a network name at least 3 characters long."
        if len(postData['desc']) > 0 and len(postData['desc']) < 10:
            error['desc'] = "If you include a description, it must be at least 10 characters long."
        if len(postData['release_date']) < 1:
            error['release_date'] = "You must provide a release date."
        elif datetime.strptime(postData['release_date'], '%Y-%m-%d') >= datetime.now():
            error['release_date'] = "The release date you choose must be in the past."
        return error

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=45)
    release_date = models.DateField()
    desc = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()