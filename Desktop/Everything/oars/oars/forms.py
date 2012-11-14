from django import forms
from oars_website.models import CourseOffer
from oars_website.views import *

class RegistrationForm(forms.Form):
	course = forms.ModelChoiceField(queryset = CourseOffer.objects.all(), empty_label=None)
	course_type = forms.ChoiceField(
		choices = (
		('Elec', 'Elective'),
		('Comp', 'Compulsary'),
		('SE','Science Elective'),
		('DE','Department Elective'),
		('HSS I', 'HSS I'),
		('HSS II', 'HSS II'),
		('ESO','ESO')
		))
	
class RollNoForm(forms.Form):
	rollNo = forms.CharField(max_length=200)

