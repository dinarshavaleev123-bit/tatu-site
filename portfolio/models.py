from django.db import models

class TattooWork(models.Model):
    CATEGORY_CHOICES = [
        ('color', 'Цветная тату'),
        ('bw', 'Чёрно-белая'),
        ('geometry', 'Геометрия'),
        ('realism', 'Реализм'),
        ('minimalism', 'Минимализм'),
    ]
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='portfolio/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title