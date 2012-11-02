# Create your views here.
from django.core.context_processors import csrf
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt, csrf_protect

@csrf_exempt
def main_page(request):
#	c = {}
#	c.update(csrf(request))
	return render_to_response(
		'main_page.html',
		{ 'user' : request.user }
	)
#	output = '''
#	<html>
#		<head><title>%s</title></head>
#		<body>
#			<h1>%s</h1><p>%s</p>
#		</body>
#	</html>
#		''' % ('OARS', 'Welcome to OARS', 'Please login to continue' )
#	return HttpResponse(output)

