import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    """ This will be our user
    - inheriting from AbstractUser gives us all fields e.g:
        * username
        * email
        * password
    How to use it:
    uses UUID for the primary key
    """
    user_id = models.UUIDField(
            primary_key=True,
            default=uuid.uuid4,
            editable=False)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)

class Conversation(models.Model):
    """
    This is a conversations between two or more users
    """
    participants = models.ManyToManyField('chats.User', related_name = 'conversations')
    conversation_id = models.UUIDField(primary_key=True,
                                       default=uuid.uuid4,
                                       editable=False)
    def __str__(self):
        """
        Used give the output a human readable format
        """
        return f"Conversation{self.conversation_id}"

class Message(models.Model):
    """
    - This is the messages to that will be contained in our model
    Relationships:
        # messages to user
        * A single message can only belong to one user: one-to-one
        * A single user can send multiple messages: to many
        # Messages to conversations
        * A single message can only belong to one conversation: one to one
        * A single conversation can have multiple messages: one to many
    """
    message_id = models.UUIDField(
            primary_key=True,
            default=uuid.uuid4,
            editable=False)
    conversation = models.ForeignKey(
            Conversation, 
            on_delete=models.CASCADE, 
            related_name='messages')
    sender = models.ForeignKey('chats.User', 
                               on_delete = models.CASCADE)
    sent_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    message_body = models.TextField()

    def __str__(self):
        return f"From{self.sender} in Conversation {self.conversation.id}"
