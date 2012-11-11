	# Create your views here.
#from django.core.context_processors import csrf
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout
from django.template import RequestContext
from oars.forms import *

@csrf_exempt
def main_page(request):
#	c = {}
#	c.update(csrf(request))
	return render_to_response(
		'main_page.html',
		RequestContext(request)
	)

@csrf_exempt
def logout_page(request):
	logout(request)
	return HttpResponseRedirect('/')

@csrf_exempt
def user_page(request, username):
	try:
		user = User.objects.get(username=username)
	except:
		raise Http404('Requested user not found.')
	variables = RequestContext(request, {
	'username': username
	})
	return render_to_response('user_page.html', variables)

@csrf_exempt
def pre_reg_page(request):
	if not request.user.is_authenticated():
		return render_to_response(
		'main_page.html',
		RequestContext(request)
		)
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			course_selected=form.cleaned_data['course']
			return HttpResponseRedirect('/')
		else:
			form = RegistrationForm()
		variables = RequestContext(request, {
		'form': form
		})
		return render_to_response('pre_reg_page.html', variables)
	else:
		form = RegistrationForm()
		variables = RequestContext(request, {
		'form': form
		})
		return render_to_response('pre_reg_page.html', variables)
		
#	output = '''
#	<html>
#		<head><title>%s</title></head>
#		<body>
#			<h1>%s</h1><p>%s</p>
#		</body>
#	</html>
#		''' % ('OARS', 'Welcome to OARS', 'Please login to continue' )
#	return HttpResponse(output)

