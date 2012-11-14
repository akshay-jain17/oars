	# Create your views here.
#from django.core.context_processors import csrf
import os
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout
from django.template import RequestContext
from oars.forms import *
from oars_website.models import *
from django.core.urlresolvers import reverse

def index(request):
    done_courses_list = DoneCourses.objects.all().order_by('-roll_no')
    context = {'latest_poll_list': done_courses_list}
    return render(request, 'gradesheet.html', context)

def detail(request, roll_no):
    courses = DoneCourses.objects.filter(roll_no).order_by('-roll_no')
    return render(request, 'gradesheet.html', done_courses_list)

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
		user = django.contrib.auth.get_user_model().objects.get(username=username)
	except:
		raise Http404('Requested user not found.')
	variables = RequestContext(request, {
	'username': username
	})
	return render_to_response('user_page.html', variables)

@csrf_exempt
def timetable_page(request):
	return render_to_response('Timetable.html', RequestContext(request))

@csrf_exempt
def student_timetable_page(request):
	if request.method == 'POST':
		form = RollNoForm(request.POST)
		if form.is_valid():
			rollNo = form.cleaned_data['rollNo']
			url = '/show_timetable/' + str(rollNo)
			return HttpResponseRedirect(url)
	else:
		form = RollNoForm()
		variables = RequestContext(request, {'form': form})
		return render_to_response('StudentTimetable.html',variables)


@csrf_exempt
def department_timetable_page(request):
	return render_to_response('DepartmentTimetable.html', RequestContext(request))

@csrf_exempt
def show_timetable(request, rollNo):
	variables = RequestContext(request, {'rollNo': rollNo})
	return render_to_response('show_timetable.html',variables)

@csrf_exempt
def pre_reg_accept(request, requestId):
	user = request.user
	if not user.is_authenticated():
		return render_to_response(
			'main_page.html',
			RequestContext(request)
		)
	if user.user_type !=2:
		return render_to_response(
			'main_page.html',
			RequestContext(request)
		)
	req = CReq.objects.get(id=requestId)
	req.status = "ACCEPTED"
	req.save()
	print req.status
	instr = Instructor.objects.get(iUser = user)
	try:
		course_offers = CourseOffer.objects.filter(instructor = instr)
	except:
		course_offers = None
	course_requests = []
	for i in course_offers:
		course_requests.extend(CReq.objects.filter(req_course = i))
	variables = RequestContext(request, {
		'c_req':course_requests,
		})
	return render_to_response('pre_reg_inspage.html', variables) 

@csrf_exempt
def pre_reg_reject(request, requestId):
	user = request.user
	if not user.is_authenticated():
		return render_to_response(
			'main_page.html',
			RequestContext(request)
		)
	if user.user_type !=2:
		return render_to_response(
			'main_page.html',
			RequestContext(request)
		)
	req = CReq.objects.get(id=requestId)
	req.status = "REJECTED"
	req.save()
	print req.status
	instr = Instructor.objects.get(iUser = user)
	try:
		course_offers = CourseOffer.objects.filter(instructor = instr)
	except:
		course_offers = None
	course_requests = []
	for i in course_offers:
		course_requests.extend(CReq.objects.filter(req_course = i))
	variables = RequestContext(request, {
		'c_req':course_requests,
		})
	return render_to_response('pre_reg_inspage.html', variables)

@csrf_exempt
def pre_reg_delete(request, requestId):
	req = CReq.objects.get(id=requestId)
	req.delete()
	return HttpResponseRedirect(reverse('oars_website.views.pre_reg_page'))

@csrf_exempt
def pre_reg_inspage(request):
	user = request.user
	if not user.is_authenticated():
		return render_to_response(
			'main_page.html',
			RequestContext(request)
		)
	if user.user_type !=2:
		return render_to_response(
			'main_page.html',
			RequestContext(request)
		)
	instr = Instructor.objects.get(iUser = user)
	try:
		course_offers = CourseOffer.objects.filter(instructor = instr)
	except:
		course_offers = None
	course_requests = []
	for i in course_offers:
		course_requests.extend(CReq.objects.filter(req_course = i))
	variables = RequestContext(request, {
		'c_req':course_requests,
		})
	return render_to_response('pre_reg_inspage.html', variables) 

@csrf_exempt
def course_view(request):
	c_offer = CourseOffer.objects.all()
	variables = RequestContext(request, {
		'c_offer':c_offer,
		})
	return render_to_response('course_view.html', variables) 

@csrf_exempt
def pre_reg_page(request):
	user = request.user
	if not user.is_authenticated():
		return render_to_response(
			'main_page.html',
			RequestContext(request)
		)
	if user.user_type != 1:
		return render_to_response(
			'main_page.html',
			RequestContext(request)
		)
	stUser = Student.objects.get(sUser = user)
	
	try:
		course_requested = CReq.objects.filter(student = stUser)
	except:
		course_requested = None
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
#		print "I was here"
		if form.is_valid():
#			print "I was here"
			cselected=form.cleaned_data['course']
			ctype = form.cleaned_data['course_type']
			course_selected = CourseOffer.objects.get(offer_id = cselected)
#			print "I was here"
			try:
#				print "I was here"
				CReq.objects.get(req_course = course_selected)
#				print "I was here"
			except:
#				print "I was here"
				new_request = CReq(
#					req_id = unicode(str(os.urandom(32)))
					student = stUser,
					status = u"WAITING",
					req_course = course_selected,
					course_type = ctype
				)
				new_request.save()
				course_requested = CReq.objects.filter(student = stUser)
#				print course_requested
		else:
			form = RegistrationForm()
		
		variables = RequestContext(request, {
		'c_req':course_requested,
		'username':user.username,
		'form': form
		})
		return render_to_response('pre_reg_page.html', variables)
	else:
		form = RegistrationForm()
		variables = RequestContext(request, {
		'c_req':course_requested,
		'username':user.username,
		'form': form
		})
		return render_to_response('pre_reg_page.html', variables)

