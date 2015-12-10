from django.db import models

class Service(models.Model):
	excellent=models.IntegerField(default=0)
	good=models.IntegerField(default=0)
	average=models.IntegerField(default=0)
	worst=models.IntegerField(default=0)

class Answers(models.Model):
	ans1=models.CharField(max_length=200)
	ans2=models.CharField(max_length=200)
	ans3=models.CharField(max_length=200)

