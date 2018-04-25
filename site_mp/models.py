from django.db import models
from django.utils import timezone

class Thing(models.Model):

    title = models.CharField(max_length=200)
    desc = models.TextField()
    email_author = models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)
    edit_date = models.DateTimeField(
            default=timezone.now)

    def edit(self):
        self.edit_date = timezone.now()
        self.save()

class Message(models.Model):

    email_user = models.CharField(max_length=200)
    text = models.TextField()
