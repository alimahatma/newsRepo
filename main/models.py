from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=200)
    category_image=models.ImageField(upload_to='imgs/')

    def __str__(self):
        return self.title
