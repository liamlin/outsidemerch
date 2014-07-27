from django.db import models


class Stage(models.Model):
    name = models.CharField(max_length=120)

    def __unicode__(self):
        return self.name


class Event(models.Model):
    time = models.DateTimeField()
    name = models.CharField(max_length=200)
    stage = models.ForeignKey(Stage, related_name="events")

    def __unicode__(self):
        return "{}".format(self.name)


class Artist(models.Model):
    name = models.CharField(max_length=120)
    event = models.ManyToManyField(Event, related_name="artists")

    def __unicode__(self):
        return "{}".format(self.name)


class Store(models.Model):
    title = models.CharField(max_length=120)
    artist = models.ForeignKey(Artist, related_name="store")

    def __unicode__(self):
        return "{}".format(self.title)


class Item(models.Model):
    price = models.FloatField()
    name = models.CharField(max_length=120)
    store = models.ForeignKey(Store, related_name="items")
    description = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "{}".format(self.name)