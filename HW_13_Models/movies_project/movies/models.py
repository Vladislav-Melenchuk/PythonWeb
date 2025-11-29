from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    country = models.CharField(max_length=100)
    poster = models.ImageField(upload_to='posters/')
    rating = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1, 6)], default=1)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-rating', 'release_date']
