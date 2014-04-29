from django.contrib.auth.models import User
from django.db import models

import urllib
import datetime


class Member(models.Model):
	# extends the functionality of Django's built-in User system
	user = models.OneToOneField(User)
	quote = models.CharField(max_length=300,
							default="I pick things up, then I put them down")
	about = models.TextField(default="")

class Entry(models.Model):
	# represents a row in a workout log
	member = models.ForeignKey(Member)
	date = models.DateField(auto_now_add=True)
	duration = models.IntegerField(default=0)   # how long this entry took
												# to complete, in seconds

MOVEMENT_CHOICES = ( # just a start, to be added to
	('NC', 'None Chosen'),
	('BP', 'Bench Press'),
	('BS', 'Back Squat'),
	('CLN', 'Clean'),
	('C&J', 'Clean and Jerk'),
	('DL', 'Deadlift'),
	('FS', 'Front Squat'),
	('GHD', 'Glute Ham Developer'),
	('HSPU', 'Hand Stand Push Up'),
	('KTE', 'Knees to Elbows'),
	('MP', 'Military Press'),
	('MU', 'Muscle Up'),
	('OHS', 'Overhead Squat'),
	('PC', 'Power Clean'),
	('PP', 'Push Press'),
	('PSN', 'Power Snatch'),
	('PU', 'Pull Up'),
	('SN', 'Snatch'),
	('TTB', 'Toes to Bar'),
)

class EntrySet(models.Model):
	# represents a single column for a row (Entry)
	entry = models.ForeignKey(Entry)
	movement = models.CharField(max_length=4, choices=MOVEMENT_CHOICES, default='NC')
	reps = models.IntegerField(default=0)
	weight = models.DecimalField(max_digits=5, decimal_places=2)
	next_set = models.ForeignKey("self", null=True, default=None, related_name="previous") 
	previous_set = models.ForeignKey("self", null=True, default=None, related_name="next")

"""
class MemberProgress(models.Model):
"""