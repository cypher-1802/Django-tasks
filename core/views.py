from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .forms import NumForm

def start(request):
	return render(request,'start.html')

def index(request):
    num=0
    form = NumForm(request.POST or None)
    if form.is_valid():
        num = form.cleaned_data.get("Number")
    context={'form':form, 'Number':range(1,num+1),}
    return render(request, 'num.html', context)
