from django.db import models
from tinymce.models import HTMLField

class Usr(models.Model):
    uname = models.CharField(max_length=20)
    upassword = models.CharField(max_length=20)
    ustate = models.CharField(max_length=50)
    ugender = models.CharField(max_length=5)
    ulogo = models.IntegerField()
    ubackground = models.IntegerField()
    umsg = models.CharField(max_length=30)
    uprivate = models.CharField(max_length=5)
    uisDelete = models.BooleanField(default=False)

    def __str__(self):
        return "%s" % self.uname


class Message(models.Model):
    mtitle = models.CharField(max_length=50)
    mbody = HTMLField()
    mdate = models.DateField()
    mread = models.IntegerField(default=0)
    mlike = models.IntegerField(default=0)
    mshare = models.IntegerField(default=0)
    mowner = models.ForeignKey(Usr)
    # misDelete = models.BooleanField()

    def __str__(self):
        return "%s" % self.mtitle

class Comt(models.Model):
    cowner = models.ForeignKey(Usr)
    cdate = models.DateField()
    cbody = HTMLField()

    def __str__(self):
        return "%d" % self.pk



