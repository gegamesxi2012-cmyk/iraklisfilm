from django.db import models

class Message(models.Model):
    phone = models.CharField(max_length=20)
    subject = models.CharField(max_length=200, blank=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject} - {self.phone}"
    
class Movie(models.Model):
    title = models.CharField(max_length=200)
    video_url = models.URLField()  # აქ შეინახება YouTube ლინკი