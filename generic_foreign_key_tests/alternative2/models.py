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


class Owner(models.Model):
    group = models.OneToOneField(Group, null=True, blank=True,
                                 on_delete=models.CASCADE)
    person = models.OneToOneField(Person, null=True, blank=True,
                                  on_delete=models.CASCADE)

    def __str__(self):
        return "Owner: {0}".format(repr(self.target))

    def save(self, **kwargs):
        assert [self.person, self.group].count(None) == 1
        return super(Owner, self).save(**kwargs)

    @property
    def target(self):
        if self.group_id is not None:
            return self.group
        if self.person_id is not None:
            return self.person
        raise AssertionError("Neither 'group' nor 'person' is set")


class Task(models.Model):
    description = models.CharField(max_length=200)

    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    def __str__(self):
        return "{0}, owned by {1}".format(self.description, repr(self.owner.target))
