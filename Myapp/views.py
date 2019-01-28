from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
# Create your views here.


#def db(request):
#	with connection.cursor() as cursor:
#		cursor.execute("")
#	pass

def home(request,a):
	print(a)
	#return HttpResponse("HEllo world")
	#a={1:'srikanth',2:'ashok',3:'vijay'}
	return render(request,"home.html",{'data':a})


def get(request):
	a=request.POST.get('name','')
	print(a)
	return HttpResponse("")
