from django import newforms as forms

class RegistrationForm(forms.Form):
	kam = forms.ModelChoiceField(queryset = CourseOffer.objects.all(), empty_label=None)
