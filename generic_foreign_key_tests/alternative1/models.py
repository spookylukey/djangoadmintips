# -*- coding: utf8 -*-

from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=200)
    creator = models.ForeignKey(Person, related_name='groups')

    def __str__(self):
        return "{0}, created by {1}".format(self.name, self.creator)


class Task(models.Model):
    description = models.CharField(max_length=200)

    owner_group = models.ForeignKey(Group, null=True, blank=True,
                                    on_delete=models.CASCADE)
    owner_person = models.ForeignKey(Person, null=True, blank=True,
                                     on_delete=models.CASCADE)

    @property
    def owner(self):
        if self.owner_group_id is not None:
            return self.owner_group
        if self.owner_person_id is not None:
            return self.owner_person
        raise AssertionError("Neither 'owner_group' nor 'owner_person' is set")

    def __str__(self):
        return "{0}, owned by {1}".format(self.description, repr(self.owner))
