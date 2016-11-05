# -*- coding: utf8 -*-

from django.contrib.contenttypes.fields import (GenericForeignKey,
                                                GenericRelation)
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Task(models.Model):
    description = models.CharField(max_length=200)

    owner_id = models.PositiveIntegerField()
    owner_type = models.ForeignKey(ContentType, on_delete=models.PROTECT)
    owner = GenericForeignKey('owner_type', 'owner_id')

    def __str__(self):
        return "{0}, owned by {1}".format(self.description, repr(self.owner))


class Person(models.Model):
    name = models.CharField(max_length=200)

    tasks = GenericRelation(Task,
                            related_query_name='person',
                            content_type_field='owner_type',
                            object_id_field='owner_id')

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=200)
    creator = models.ForeignKey(Person, related_name='groups')

    def __str__(self):
        return "{0}, created by {1}".format(self.name, self.creator)
