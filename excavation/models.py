from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

class Grabung(models.Model):
	nummer = models.IntegerField(unique=True)
	name = models.CharField(max_length=50)

	def __unicode__(self):
		return unicode(self.nummer) or u''

class Bearbeiter(models.Model):
	vorname = models.CharField(max_length=50)
	name = models.CharField(max_length=50)

	def __unicode__(self):
		return self.name


class Befund(models.Model):
	nummer = models.IntegerField(unique=True)
	deutung = models.CharField(max_length=50)
	datierung = models.CharField(max_length=50, blank = True)
	masse = models.CharField(max_length=100, blank = True)
	kurzbeschreibung = models.TextField(max_length=250)
	datum = models.DateField()
	bearbeiter = models.ForeignKey(Bearbeiter, null=True, on_delete=models.CASCADE)
	ausgrabung = models.ForeignKey(Grabung, on_delete=models.CASCADE)
	bemerkung = models.CharField(max_length=250, blank=True, null = True)

	def __unicode__(self):
		return unicode(self.nummer) or u''

class Profil(models.Model):
	nummer = models.IntegerField(unique=True)
	richtung = models.CharField(max_length=50)
	datum = models.DateField()
	bearbeiter = models.ForeignKey(Bearbeiter, null=True, on_delete=models.CASCADE)
	befund = models.ManyToManyField(Befund)
	bemerkung = models.CharField(max_length=250, blank=True, null = True)

	def __unicode__(self):
		return unicode(self.nummer) or u''

class Foto(models.Model):
	nummer = models.IntegerField(unique=True)
	richtung = models.CharField(max_length=50)
	profil = models.ManyToManyField(Profil, blank = True)
	planum = models.CharField(max_length=20, blank = True) 
	datum = datum = models.DateField()
	bearbeiter = models.ForeignKey(Bearbeiter, null=True, on_delete=models.CASCADE)
	befund = models.ManyToManyField(Befund)
	bemerkung = models.CharField(max_length=250, blank=True, null = True)

	def __unicode__(self):
		return unicode(self.nummer) or u''









