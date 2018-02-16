# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
	title 		= models.CharField(max_length=150)
	description = models.TextField()
	date_add 	= models.DateTimeField(auto_now_add=True)
	date_change = models.DateTimeField(auto_now=True)
	public 		= models.BooleanField()
	author		= models.ForeignKey(User)

	def __str__(self):
		return self.title