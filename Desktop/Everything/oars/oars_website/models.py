from django.db import models

# Create your models here.

class Department(models.Model):
	dept_id = models.CharField(max_length = 20, unique = True)
	name = models.CharField(max_length = 100)


class Student(models.Model):
	roll_no = models.CharField(max_length=200)
	name = models.CharField(max_length = 200)
	program = models.CharField(max_length = 200)
	department = models.ForeignKey(Department)

class Instructor(models.Model):
	instructor_id = models.CharField(max_length = 200)
	name = models.CharField(max_length = 200)
	department = models.ForeignKey(Department)
		
class Course(models.Model):
	course_no = models.CharField(max_length = 20, unique = True)
	title = models.CharField(max_length = 200)
	department = models.ForeignKey(Department)
	units = models.IntegerField()
	
class CourseOffer(models.Model):
	offer_id = models.CharField(max_length = 20, unique = True)
	course = models.ForeignKey(Course)
	instructor = models.ForeignKey(Instructor)
	note = models.CharField(max_length = 200)
	time = models.CharField(max_length = 200)

class CourseRequest(models.Model):
	student = models.ForeignKey(Student)
	status = models.CharField(max_length = 50)
	course = models.ForeignKey(CourseOffer) 
