from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.contrib import auth
#from django.contrib.auth.models import User


#class UserProfile(models.Model):
#    # This field is required.
#    user = models.OneToOneField(User)

#    # Other fields here
#    user_type = models.IntegerField()

## Create your models here.


from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class MyUserManager(BaseUserManager):
    def create_user(self, username, user_type, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not username:
            raise ValueError('Users must have an username')

        user = self.model(
            username=username,
            user_type=user_type,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, user_type, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(username,
            password=password,
            user_type=user_type
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    username = models.CharField(
        verbose_name='username',
        max_length=255,
        unique=True,
        db_index=True,
    )
    user_type = models.IntegerField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['user_type']

    def get_full_name(self):
        # The user is identified by their email address
        return self.username

    def get_short_name(self):
        # The user is identified by their email address
        return self.username

    def __unicode__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Department(models.Model):
	dept_id = models.CharField(max_length = 20, unique = True)
	name = models.CharField(max_length = 100)
	def __unicode__(self):
		return self.name

def validate_student(value):
	user = auth.get_user_model().objects.get(id=value)
	if user.user_type != 1:
		raise ValidationError(u'%s is not an student' %user.username)

def validate_instructor(value):
#	if value.user_type != 2:
	user = auth.get_user_model().objects.get(id=value)
	if user.user_type != 2:
		raise ValidationError(u'%s is not an Instructor' % user.username)

class Student(models.Model):
	roll_no = models.CharField(max_length=200, unique = True)
	sUser = models.ForeignKey(settings.AUTH_USER_MODEL, unique = True, validators = [validate_student])
	name = models.CharField(max_length = 200)
	program = models.CharField(max_length = 200)
	department = models.ForeignKey(Department)
	def __unicode__(self):
		return self.name

class Instructor(models.Model):
	instructor_id = models.CharField(max_length = 200, unique = True)
	iUser =  models.ForeignKey(settings.AUTH_USER_MODEL, unique = True, validators = [validate_instructor])
	name = models.CharField(max_length = 200)
	department = models.ForeignKey(Department)
	def __unicode__(self):
		return self.name


class Course(models.Model):
	course_no = models.CharField(max_length = 20, unique = True)
	title = models.CharField(max_length = 200)
	department = models.ForeignKey(Department)
	units = models.IntegerField()
	def __unicode__(self):
		return self.course_no

class CReq(models.Model):
#	req_id = models.CharField(max_length = 50, unique = True)
	student = models.ForeignKey(Student)
	status = models.CharField(max_length = 50)
	req_course = models.ForeignKey('CourseOffer')
	
	def __unicode__(self):
		return self.req_course.offer_id
	
	@classmethod
	def create(cls, request_id, student, status, req_course):
#		print "I was here"
		request_course = cls(request_id = request_id, student = student, status = status, req_course = req_course)
		return request_course
	
class CourseOffer(models.Model):
	offer_id = models.CharField(max_length = 20, unique = True)
	course = models.ForeignKey(Course)
	instructor = models.ForeignKey(Instructor)
	note = models.CharField(max_length = 200)
	time = models.CharField(max_length = 200)
	def __unicode__(self):
		return self.offer_id

class DoneCourses(models.Model):
	roll_no = models.CharField(max_length=10)
	course_no = models.CharField(max_length=8)
	course_name = models.CharField(max_length=50)
	course_grade = models.IntegerField()
	course_year = models.IntegerField()
	course_semester = models.IntegerField()
	def __unicode__(self):
		return self.roll_no
	def grade_letter(self):
		return self.course_grade
