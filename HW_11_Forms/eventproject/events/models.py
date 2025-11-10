from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField()

    def __str__(self):
        return self.name


class Participant(models.Model):
    event = models.ForeignKey(Event, related_name='participants', on_delete=models.CASCADE)
    email = models.EmailField()

    def __str__(self):
        return self.email
