from django.db import models

class Login(models.Model):
    number = models.IntegerField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.password


