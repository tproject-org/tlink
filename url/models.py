from django.db import models

# Create your models here.

class URL(models.Model):
    url = models.URLField(max_length=1000, unique=True)
    short_url = models.CharField(max_length=1000, blank=True)
    number_of_view = models.IntegerField(default=0)
    owner = models.ForeignKey('auth.User',  on_delete=models.CASCADE)

    def __str__(self):
        return self.url