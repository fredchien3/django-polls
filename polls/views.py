from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
  return HttpResponse("Hello World! You're at the polls index")

def fred(request):
  return HttpResponse("hello fred")

def detail(request, question_id):
  return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
  return HttpResponse("You're looking at the results of question %s." % question_id)

def vote(request, question_id):
  return HttpResponse("You're voting on %s" % question_id)