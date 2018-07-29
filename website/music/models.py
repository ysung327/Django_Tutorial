from django.db import models
from django.urls import reverse

# Create your models here. Blueprint of your database.

class Album(models.Model):
    artist = models.CharField(max_length=250)  #This is gonna be columns of data.
    album_title = models.CharField(max_length=500)
    gerne = models.CharField(max_length=100)
    album_logo = models.FileField()

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk' : self.pk})

    def __str__(self):
        return self.album_title + ' - ' + self.artist


class Song(models.Model):

    ''' ForeignKey relates models into N:1
     Which Album includes number of Songs. So, each song is set member of album.
     When certain Album is deleted, then their songs gonna missed. so, on_delete_CASCADE makes the songs deleted.
    '''

    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title= models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title