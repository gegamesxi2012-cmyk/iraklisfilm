from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, default='')
    video_url = models.URLField()

    def __str__(self):
        return self.title

class Message(models.Model):
    subject = models.CharField(max_length=200)
    text = models.TextField()
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)