from tkinter import CASCADE
from django.db import models
from core import models as core_models

class Conversation(core_models.TimeStampedModel):

    participants = models.ManyToManyField("users.User", related_name = "conversations", blank=True)

    def __str__(self):
        return str(self.created)

class Message(core_models.TimeStampedModel):

    message = models.TextField()
    user = models.ForeignKey("users.User", related_name = "messages", on_delete=models.CASCADE)
    conversation = models.ForeignKey("Conversation", related_name = "messages", on_delete=CASCADE)

    def __str__(self):
        return f'{self.user} says: {self.message}'
