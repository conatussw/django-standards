from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(default=None, blank=True, null=True)
    featured_image = models.ImageField(
        upload_to='images/%Y/%m/%d/', default=None, blank=True, null=True)
