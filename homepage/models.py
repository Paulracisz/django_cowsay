from django.db import models

# Create your models here.
class CowSpeech(models.Model):
    user_text = models.TextField(max_length=100, default="Enter text")

    def __str__(self):
        return self.user_text 

