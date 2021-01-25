from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class ChatMessage(models.Model):
    """Create table in DB"""
    text = models.CharField('tresc wiadomosci', max_length=250)
    textDate = models.DateTimeField('data publikacji', auto_now_add=True)
    textAuthor = models.ForeignKey(User, on_delete=models.CASCADE)  # on_delete is required parameter and it's not set by default

    class Meta:
        verbose_name = u'wiadomość'
        verbose_name_plural = u'wiadomości'
        ordering = ['-textDate']        # newest messages on the top

    def __str__(self):                  # auto-presentation - show messages
        return self.text