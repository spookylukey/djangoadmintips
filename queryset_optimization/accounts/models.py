from django.db import models


class Profile(models.Model):
    user = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
