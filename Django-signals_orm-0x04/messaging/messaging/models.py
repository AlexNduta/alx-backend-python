from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.


class User(AbstractUser):
    pass


class Message(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE, 
                               related_name= 'sent_messages')
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 on_delete=models.CASCADE,
                                 related_name = 'received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"from {self.sender} to {self.receiver}"

class Notification(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name = 'notifications')
    message = models.OneToOneField(Message,
                                   on_delete=models.CASCADE, 
                                   related_name = 'messages')
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.user} about message from{self.message.sender}"


