from django.db import models

# Create your models here.
class predictor(models.Model):
    firstname = models.CharField(max_length=15)
    lastname = models.CharField(max_length=15)
    age = models.IntegerField()
    heightfeet = models.IntegerField()
    heightinches = models.IntegerField()

    def __str__(self):
        return self.firstname
