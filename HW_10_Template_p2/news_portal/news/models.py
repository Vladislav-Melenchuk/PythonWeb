from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class News(models.Model):
    category = models.ForeignKey(Category, related_name='news', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='news_images/')
    content = models.TextField()

    def __str__(self):
        return self.title
