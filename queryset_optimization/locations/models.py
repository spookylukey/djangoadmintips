from django.db import models

from accounts.models import Profile


class Location(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE,
                              related_name='locations_as_owner')
    postcode = models.CharField("postcode", max_length=11, blank=True)
    tenants = models.ManyToManyField(Profile, blank=True,
                                     related_name='locations_as_tenant')

    def __str__(self):
        return self.postcode
