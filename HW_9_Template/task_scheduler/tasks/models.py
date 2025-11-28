from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    time = models.TimeField()
    completed = models.BooleanField(default=False)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.title
