from django.db import models
from django.urls import reverse
from PIL import Image

# Create your models here.
class Post(models.Model):
    objects: models.Manager()
    image = models.ImageField(default='posts_pics/default.jpg', upload_to='posts_pics')
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def get_absolute_url(self):
        return reverse('post-details', kwargs={'pk': self.pk})
