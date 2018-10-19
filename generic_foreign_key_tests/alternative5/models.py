# -*- coding: utf8 -*-

from django.db import models


class Owner(models.Model):
    # Not strictly speaking a necessary part of this solution,
    # but is a nice refinement.
    name = models.CharField(max_length=200)

    class Meta:
        abstract = True


class Person(Owner):
    def __str__(self):
        return self.name


class Group(Owner):
    creator = models.ForeignKey(Person, related_name='groups')

    def __str__(self):
        return "{0}, created by {1}".format(self.name, self.creator)


class Task(models.Model):
    description = models.CharField(max_length=200)

    class Meta:
        abstract = True

    def __str__(self):
        return "{0}, owned by {1}".format(self.description, repr(self.owner))


class PersonTask(Task):
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)


class GroupTask(Task):
    owner = models.ForeignKey(Group, on_delete=models.CASCADE)
