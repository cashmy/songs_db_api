from django.db import models


# Create your models here.
# noinspection PyStatementEffect
class Song(models.Model):
    track = models.IntegerField(default=0)
    title = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    album = models.CharField(max_length=50)
    release_date = models.DateField(null=True, blank=True)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title
