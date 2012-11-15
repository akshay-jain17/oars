import os.path
from django.conf.urls import patterns, include, url
from oars_website.views import *

site_media = os.path.join(
	os.path.dirname(__file__), 'site_media'
)

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'oars.views.home', name='home'),
    # url(r'^oars/', include('oars.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^$', main_page),
    (r'^user/(\w+)/$', user_page),
    (r'^login/$', 'django.contrib.auth.views.login'),
	(r'^logout/$', logout_page),
	(r'^pre-reg/$', pre_reg_page),
	(r'^course-view/$', course_view),
	(r'^pre-reg-inr/$', pre_reg_inspage),
	(r'^pre-reg1/delete/(\w+)/$', pre_reg_delete),
	(r'^pre-reg1/accept/(\w+)/$', pre_reg_accept),
	(r'^pre-reg1/reject/(\w+)/$', pre_reg_reject),
	(r'^timetable/$', timetable_page),
	(r'^student_timetable/$', student_timetable_page),
    (r'^department_timetable/$', department_timetable_page),
    (r'^show_timetable/(\w+)/$', show_timetable),
	url(r'^gradesheet/$', index, name='index'),
	(r'^add_course/$', add_course),
	url(r'^gradesheet/(?P<roll_no>\d+)/$', detail, name='detail'),
	(r'^site_media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': site_media }),
)
