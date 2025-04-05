from django.db import models

class Property(models.Model):
    TYPE_CHOICES = [
        ('flat', 'Квартира'),
        ('commercial', 'Коммерция'),
    ]

    title = models.CharField(max_length=255)
    complex_name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    image = models.ImageField(upload_to='property_images/')
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)

    def __str__(self):
        return self.title
