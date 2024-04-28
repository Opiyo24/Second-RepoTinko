from django.db import models

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length = 200)
    capital = models.IntegerField(default=1000)


    def __str__(self):
        return self.name
    

class Play(models.Model):
    player = models.CharField(max_length = 200)
    score = models.IntegerField()
    response = models.BooleanField(default=False)
    score2 = models.IntegerField()
    response2 = models.BooleanField(default=False)
    score3 = models.IntegerField()
    response2 = models.BooleanField(default=False)

    def __str__(self):
        return self.player