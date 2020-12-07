# -*- coding: utf8 -*-

from django.db import models


class Owner(models.Model):

    def __str__(self):
        return "Owner: {0}".format(repr(self.target))

    @property
    def target(self):
        if getattr(self, 'group', None) is not None:
            return self.group
        if getattr(self, 'person', None) is not None:
            return self.person
        return None


class Person(Owner):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Group(Owner):
    name = models.CharField(max_length=200)
    creator = models.ForeignKey(Person, related_name='groups', on_delete=models.PROTECT)

    def __str__(self):
        return "{0}, created by {1}".format(self.name, self.creator)


class Task(models.Model):
    description = models.CharField(max_length=200)

    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    def __str__(self):
        return "{0}, owned by {1}".format(self.description, repr(self.owner.target))
