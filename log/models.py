from django.db import models

class Log(models.Model):
	user = models.ForeignKey(u'User', blank=True, null=True)
	error_type = models.ForeignKey(u'Category', blank=True, null=True)
	message = models.CharField(u'Message', max_length=200)
	log_date = models.DateTimeField('date published')

	def __unicode__(self):
		return self.message

class User(models.Model):
	name = models.CharField(u'Name', max_length=50)
	email = models.CharField(u'Email', max_length=50)
	userid = models.CharField(u'User_ID', max_length=50)

	def __unicode__(self):
		return self.name

class Category(models.Model):
	title = models.CharField(u'Title', max_length=50)

	def __unicode__(self):
		return self.title
