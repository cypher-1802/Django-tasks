from django.http import HttpResponse

def start(request):
	return HttpResponse("<h1><center>Hello !!!</center></h1>")