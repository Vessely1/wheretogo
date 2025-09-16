from django.db import models


class Place(models.Model):
    PLACE_TYPES = [
        ('restaurant', 'Ресторан'),
        ('cafe', 'Кафе'),
        ('park', 'Парк'),
        ('cinema', 'Кінотеатр'),
        ('museum', 'Музей'),
        ('other', 'Інше'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    place_type = models.CharField(max_length=20, choices=PLACE_TYPES)
    location = models.CharField(max_length=100, blank=True, null=True)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='places/', default='places/default.jpg')

    def __str__(self):
        return self.name