from .models import Message, Notification
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Message) # connect our function to a signal
def create_message_notification(sender, instance, created, **kwargs):
    """
    A sinal handler that sutomaticaly creates a new notification
    whenever a new message is created
    - post_save is sent by django after the .save() is called
    args:
        'instance'-> The actual message that was sent
        'created'-> Boolean that will be true only on  first save
        ''
    """
    # our conditions only run for brand new messages
    if created:
        # if the message is new, we create a notification object linking the message to the receiver
        Notification.object.create(
                user=instance.receiver, # notify the receiver of the message
                message=istance # link the notification to the message that triggered it
                )

