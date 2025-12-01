from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    country = models.CharField(max_length=100)
    poster = models.ImageField(upload_to='posters/')
    rating = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1, 6)], default=1)
    genres = models.ManyToManyField(Genre, related_name='movies')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-rating', 'release_date']

class Review(models.Model):
    movie = models.ForeignKey(Movie, related_name='reviews', on_delete=models.CASCADE)
    user_name = models.CharField(max_length=255, default='testUser0')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        permissions = [
            ("can_moderate_reviews", "Може модерувати відгуки"),
        ]

    def save(self, *args, **kwargs):
        if not self.user_name:
            last_review = Review.objects.filter(movie=self.movie).last()
            last_index = int(last_review.user_name[-1]) if last_review else 0
            self.user_name = f'testUser{last_index + 1}'
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Review by {self.user_name}'

