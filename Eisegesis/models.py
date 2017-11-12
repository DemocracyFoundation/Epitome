from __future__ import unicode_literals
import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, Group


class PollCat(models.Model):
	PCAT_CAT = models.CharField(max_length=100)                            # the category of the poll
	def __unicode__(self):
		return self.PCAT_CAT


class Polls(models.Model):
	P_CODE = models.CharField(max_length=200)                              # the code of the poll
	P_TITLE = models.CharField(max_length=100)                             # the title of the poll
	P_SHRBODY = models.CharField(max_length=300)                           # the short body of the poll
	P_BODY = models.CharField(max_length=1000)                             # the body (main text) of the poll
	P_CREATION = models.DateTimeField(default = timezone.now())            # the creation date and time of the poll
	P_STARTDT = models.DateTimeField()                                     # the starting date and time of the poll
	P_ENDDT = models.DateTimeField()                                       # the ending date and time of the poll
	P_DURATION = models.IntegerField(default=0)                            # the duration of the poll
	P_CODE2 = models.CharField(max_length=200, blank = True)               # the code2 of the poll (protocol number, approval number)
	USER_CREATORID = models.ForeignKey(User, on_delete=models.CASCADE)     # the user (admin) who created the poll
	UGRP_GROUPID = models.ForeignKey(Group, on_delete=models.CASCADE)      # the group of the user that created the poll
	PCAT_CAT = models.ForeignKey(PollCat)                                  # the category of the poll
	#PCHOICE_CHOICE = models.ForeignKey(PollChoice)                        # the voting choices of the poll
	def __unicode__(self): 
		return "%s %s" % (self.P_TITLE, self.P_BODY)


class PollChoice(models.Model):
	#PCHOICE_CHOICE = models.IntegerField(default=0)                       # the voting choices of the poll
	polls = models.ForeignKey(Polls, related_name='PChoice')
	PCHOICE_CHOICE = models.CharField(max_length=100)
	PCHOICE_VOTES = models.IntegerField(default=0)
	def __unicode__(self):
		return self.PCHOICE_CHOICE


class Voter(models.Model):
	user = models.ForeignKey(User)
	Polls = models.ForeignKey(Polls)
