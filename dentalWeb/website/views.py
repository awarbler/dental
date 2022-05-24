from django.shortcuts import render

# Create your views here.
#  pass request to app 
def home(request):
	#  return render , we ar rendering request, request from home.html, and context variable to pass things in
		return render (request, 'home.html', {})