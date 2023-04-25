from django.db import models

# Create your models here.
class App(models.Model):
    app_name = models.CharField(max_length=200)
    detail = models.TextField()
    link = models.TextField()
    images = models.TextField()
    school = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    money = models.IntegerField()
    value = models.FloatField()
    machine = models.CharField(max_length=200)

    def __str__(self):
        return self.app_name