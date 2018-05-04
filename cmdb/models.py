from django.db import models
class Information(models.Model):
    SN = models.CharField(max_length=30)
    privateip = models.GenericIPAddressField()
    publicip = models.GenericIPAddressField()
    use = models.TextField()
    os = models.CharField(max_length=30,default='')
    IDCid = models.CharField(max_length=30,default='')
    locate = models.CharField(max_length=30,default='')
    cpu = models.CharField(max_length=50)
    memory = models.CharField(max_length=50)
    datadisk = models.CharField(max_length=30)
    time = models.DateTimeField()

    def __unicode__(self):
        return self.SN
