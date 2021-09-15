from django.shortcuts import render
from Registration.models import Registration
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
# Create your views here.
def index(request):
	if request.method == "POST":
		username = request.POST.get('username')
		fname = request.POST.get('fname')
		lname = request.POST.get('lname')
		email = request.POST.get('email')
		contact = request.POST.get('contact')
		gender = request.POST.get('gender')
		pswd = request.POST.get('pswd')
		pswd_rep = request.POST.get('pswd-rep')

		#Checking for uniqueness of Username, contact details and email
		if (Registration.objects.filter(username=username).first()is not None):
			return render(request, "signup.html", {"message":"User already exists with that username!!! Please enter different username."})
		if (Registration.objects.filter(email=email).first()is not None):
			return render(request, "signup.html", {"message":"User already exists with that Email!!! Please enter different Email ID."})
		if (Registration.objects.filter(contact=contact).first()is not None):
			return render(request, "signup.html", {"message":"User already exists with that contact number!!! Please enter different contact number."})
		if pswd!=pswd_rep:
			return render(request, "signup.html", {"message":"Password don't match!!! Please enter again."})

		#Creating user
		new_user = User.objects.create_user(username=username, first_name=fname, last_name=lname, email=email, password=pswd)
		new_user.save()

		#Creating user in database
		s_user=Registration(username=username, first_name=fname, last_name=lname, email=email, contact=contact, gender=gender, passwd=pswd, conf_passwd=pswd_rep)
		s_user.save()

		data=Registration.objects.filter(username=username).first()
		user={'data':data}
		return render(request,"success.html",user)
	return render(request, "signup.html")


def login(request):
	if request.method == "POST":
		username = request.POST.get('username')
		pswd = request.POST.get('pswd')
		data = Registration.objects.filter(username=username).first()

		if authenticate(username=username, password=pswd) is not None:
			user={'data':data}
			return render(request,"success.html", user)
		else:
			return render(request, "login.html", {"message":"Invalid credentials!!! If you are not a registered user please register."})
	return render(request, "login.html")


def search(request):
	if request.method == "POST":
		email = request.POST.get('email')
		data = Registration.objects.filter(email=email).first()

		if data is not None:
			user = {'data':data}
			return render(request,"searchpg.html",user)
		else:
			return render(request, "search.html", {"message":"User not found!!!"})

	return render(request, "search.html")

