from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
	return render(request,"home.html")


def Checkintothepolygon(request):
	# here we can get two points(latitude and longitude) from request and then we fetch all the polygon points
	# from the Location model and use below mentioned algorithms to match the points and if match we return the Dealer 
	# or provider info
	# 
	# http://alienryderflex.com/polygon/
	# http://www.geeksforgeeks.org/how-to-check-if-a-given-point-lies-inside-a-polygon/
	pass