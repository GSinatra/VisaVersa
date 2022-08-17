from django.http import HttpResponse
from django.shortcuts import render

def textarea(request):
	return render(request, 'textarea.html')

def reverse(request):
	get_message = request.GET['message']
	reversed_message = get_message[::-1]
	return render(request, 'reverse.html', {'message': get_message,'reversed_message': reversed_message, 'data': len(get_message.split())})
