from django.db import models

# Create your models here.
class User(models.Model):
	username = models.CharField(max_length=30,default='')
	password = models.CharField(max_length=30,default='')
	email = models.EmailField(max_length=16,default='')
	ctime = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.username
