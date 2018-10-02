from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=50)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name

class Art(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    created = models.DateField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.title
