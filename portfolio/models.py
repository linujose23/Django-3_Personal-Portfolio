from django.db import models

# Create your models here.


class portfolio_model(models.Model):
    title = models.CharField(max_length=120)
    desc = models.CharField(max_length=200)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)

    # def __str__(self):
    #     return title
