from django.db import models

# Create your models here.

class URL(models.Model):
    url = models.CharField(max_length=1000)
    short_url = models.CharField(max_length=1000)
    number_of_view = models.IntegerField(default=0)
    owner = models.ForeignKey('auth.User', related_name='urls', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.url