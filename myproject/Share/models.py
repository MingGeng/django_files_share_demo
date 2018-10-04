from django.db import models
from datetime import datetime


class Upload(models.Model):
    DownloadDocount = models.IntegerField(verbose_name=u"Check times", default=0)
    code = models.CharField(max_length=8,verbose_name=u"code")
    # do not use datetime.now()!!
    Datatime = models.DateTimeField(default=datetime.now,verbose_name=u"add time") 
    path = models.CharField(max_length=32,verbose_name=u"download path")
    name = models.CharField(max_length=32,verbose_name=u"file name",default="")
    Filesize = models.CharField(max_length=10,verbose_name=u"file size")
    PCIP = models.CharField(max_length=32,verbose_name=u"IP address",default="")

    class Meta():
        verbose_name="download"
        db_table="download"

    def __str__(self):
        return self.name



