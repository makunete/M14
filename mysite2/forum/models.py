from __future__ import unicode_literals

from django.db import models

from datetime import datetime

# Create your models here.
class Login(models.Model):
	"""docstring for Login"""
	usuari=models.CharField(max_length=20)
	email=models.CharField(max_length=20)
	contrasenya=models.CharField(max_length=64)
	def __str__(self):
		return self.usuari

class Missatges(models.Model):
	"""docstring for Missatges"""
	usuari=models.ForeignKey(Login)
	text=models.CharField(max_length=140)
	data=models.DateTimeField(auto_now_add=True,blank=True)

	def __str__(self):
		return self.text


class Hashtags(models.Model):
	"""docstring for Hashtags"""
	nom_hashtag=models.CharField(max_length=20)
	missatge = models.ManyToManyField(Missatges)
	
	def __str__(self):
		return self.nom_hashtag	