from django.db import models

# Create your models here.

class Student(models.Model):
	roll_no = models.CharField(max_length=200)
	name = models.CharField(max_length = 200)
	program = models.CharField(max_length = 200)
	department = models.CharField(max_length = 200)

class Instructor(models.Model):
		instructor_id = models.CharField(max_length = 200)
		name = models.CharField(max_length = 200)
		department = models.CharField(max_length = 200)
