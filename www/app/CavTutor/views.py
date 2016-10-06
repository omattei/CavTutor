from django.shortcuts import render
from urllib.request import urlopen

import json
#import requests

UX_BASE = 'http://ux:8000/'

# Create your views here.

def index(request):

    context = {
            "title" : "CavTutor: A Tutoring Marketplace",
            "models" : ['institutions', 'users', 'courses', 'tutors', 'tutees'],
        }

    return render(request, 'CavTutor/index.html', context)


"""
    Institutions
"""
def institution_list(request):

    json_data = urlopen(UX_BASE + 'institutions/').read().decode('utf-8')
    context = {'institutions' : json.loads(json_data) }

    return render(request, 'CavTutor/institution-list.html', context)

def institution_detail(request, inst_id):

    json_data = urlopen(UX_BASE + 'institutions/' + inst_id).read().decode('utf-8')
    context = {'institution' : json.loads(json_data) }

    return render(request, 'CavTutor/institution-detail.html', context)

"""
    Course
"""
def course_list(request):

    json_data = urlopen(UX_BASE + 'courses/').read().decode('utf-8')
    context = {'courses' : json.loads(json_data) }

    return render(request, 'CavTutor/course-list.html', context)

def course_detail(request, inst_id):

    json_data = urlopen(UX_BASE + 'courses/' + inst_id).read().decode('utf-8')
    context = {'course' : json.loads(json_data) }

    return render(request, 'CavTutor/course-detail.html', context)

"""
    Tutor
"""
def tutor_list(request):

    json_data = urlopen(UX_BASE + 'tutors/').read().decode('utf-8')
    context = {'tutors' : json.loads(json_data) }

    return render(request, 'CavTutor/tutor-list.html', context)

def tutor_detail(request, inst_id):

    json_data = urlopen(UX_BASE + 'tutors/' + inst_id).read().decode('utf-8')
    context = {'tutor' : json.loads(json_data) }

    return render(request, 'CavTutor/tutor-detail.html', context)

"""
    Tutee
"""
def tutee_list(request):

    json_data = urlopen(UX_BASE + 'tutees/').read().decode('utf-8')
    context = {'tutees' : json.loads(json_data) }

    return render(request, 'CavTutor/tutee-list.html', context)

def tutee_detail(request, inst_id):

    json_data = urlopen(UX_BASE + 'tutees/' + inst_id).read().decode('utf-8')
    context = {'tutee' : json.loads(json_data) }

    return render(request, 'CavTutor/tutee-detail.html', context)

"""
    User
"""
def user_list(request):

    json_data = urlopen(UX_BASE + 'users/').read().decode('utf-8')
    context = {'users' : json.loads(json_data) }

    return render(request, 'CavTutor/user-list.html', context)

def user_detail(request, inst_id):

    json_data = urlopen(UX_BASE + 'users/' + inst_id).read().decode('utf-8')
    context = {'user' : json.loads(json_data) }

    return render(request, 'CavTutor/user-detail.html', context)