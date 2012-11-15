"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.utils import unittest
from django.test.client import Client

class SimpleTest(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()
        self.client.login(username='ekta', password='ekta')

    def test_login(self):
        # Issue a Post request.
        response = self.client.post('/login/', {'name': 'ekta', 'passwd': 'ekta'})

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

    def test_timetable(self):
        # Issue a GET request.
        response = self.client.get('/timetable/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

    def test_course_view(self):
        # Issue a GET request.
        response = self.client.get('/course-view/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

    def test_pre_reg(self):
        # Issue a GET request.
        response = self.client.get('/pre-reg/' )

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

#    def test_gradesheet(self):
#        # Issue a GET request.
#        response = self.client.get('/gradesheet/' )

#        # Check that the response is 200 OK.
#        self.assertEqual(response.status_code, 200)

    def test_department_timetable(self):
        # Issue a GET request.
        response = self.client.get('/department_timetable/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

    def test_student_timetable(self):
        # Issue a GET request.
        response = self.client.get('/student_timetable/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        # Issue a GET request.
        response = self.client.get('/logout/' )

        # Check that the response is 302 OK.
        self.assertEqual(response.status_code, 302)

    def test_option(self):
        # Issue a GET request.
        response = self.client.put('/pre-reg/', {'Course:': 'CS100', 'Course type:': 'Comp'})

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

