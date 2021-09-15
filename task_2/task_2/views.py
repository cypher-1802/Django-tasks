from django.shortcuts import render

def index(request):
    if request.method == "POST":
        number = request.POST.get("Number")
        context=[i for i in range(1, int(number)+1)]
        return render(request, 'result.html', {'context':context})
    return render(request, 'num.html')