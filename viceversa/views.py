from django.http import HttpResponse
from django.shortcuts import render

def textarea(request):
	return render(request, 'textarea.html')