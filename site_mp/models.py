from django.db import models
from django.utils import timezone

class Thing(models.Model):

    title = models.CharField(max_length=200)
    desc = models.TextField()
    email_author = models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)
    edit_date = models.DateTimeField(
            blank=True, null=True)

    def edit(self):
        self.edit_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
