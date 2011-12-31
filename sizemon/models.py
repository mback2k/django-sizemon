from django.db import models

class Snapshot(models.Model):
    crdate = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return unicode(self.crdate)

class Path(models.Model):
    snapshot = models.ForeignKey(Snapshot)
    path = models.TextField()
    size = models.IntegerField()

    def __unicode__(self):
        return unicode(self.path)
