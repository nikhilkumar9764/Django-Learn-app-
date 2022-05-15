from ckeditor.fields import RichTextField
from django.db import models
from datetime import *
# Create your models here.
from ckeditor import *

class Youtuber(models.Model):
    crew_choices = (
        ('solo', 'solo'),
        ('small', 'small'),
        ('large', 'large')
    )

    camera_choices = (
        ('nikon', 'nikon'),
        ('sony', 'sony'),
        ('canon', 'canon'),
        ('fuji', 'fuji'),
        ('panasonic', 'panasonic'),
        ('red', 'red'),
        ('others', 'others'),
    )

    category_choices = (
        ('code', 'code'),
        ('movie_review', 'movie_review'),
        ('vlogs', 'vlogs'),
        ('comedy', 'comedy'),
        ('gaming', 'gaming'),
        ('film_making', 'film_making'),
        ('cooking', 'cooking'),
    )

    name = models.CharField(max_length=255)
    price = models.IntegerField()
    photo = models.ImageField(upload_to='ytubers/%Y/%m')
    video_url = models.URLField()
    description = RichTextField()
    city = models.CharField(max_length=255)
    age = models.IntegerField()
    height = models.IntegerField()
    crew = models.CharField(choices=crew_choices,max_length=255)
    camera_type = models.CharField(choices=camera_choices,max_length=255)
    subs_count = models.IntegerField()
    category = models.CharField(choices=category_choices,max_length=255)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)
