from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=300, blank=True)
    photo = models.ImageField(upload_to='api_server/static/photo', blank=True)
    date = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=True)

    def __str__(self):
        return self.title
