from django.db import models

# Create your models here.

class Artist(models.Model):
    name_kor = models.CharField(max_length=250)
    name_eng = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    detail = models.CharField(max_length=1000)
    artist_photo = models.CharField(max_length=500)

    def __str__(self):
        return self.name_eng


class Art(models.Model):
    #artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    art_title = models.CharField(max_length=500)
    theme = models.CharField(max_length=250)
    preview = models.CharField(max_length=500)
    size = models.CharField(max_length=250)
    media = models.CharField(max_length=250)
    frame = models.CharField(max_length=250)
    edition = models.CharField(max_length=250)
    detail = models.CharField(max_length=1000)

    def __str__(self):
        return self.art_title + ' - ' + self.artist


