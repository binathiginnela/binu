from django.shortcuts import render

# Create your views here.

def home(request):
	return render(request,'html/home.html')

def about(request):
	return render(request,'html/about.html')

def contactus(request):
	return render(request,'html/contactus.html')

def login(request):
	return render(request,'html/login.html')

def register(request):
	if request.method=="POST":
		u=request.POST['uname']
		p=request.POST['pd']
		m=request.POST['eml']
		a=request.POST['ag']
		d={'us':u,'em':m,'age':a,'ps':p}
		return render(request,'html/details.html',{'d':d})
	return render(request,'html/register.html')
