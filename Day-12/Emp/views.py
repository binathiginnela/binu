from django.shortcuts import render
from Emp.models import UsrRg

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

def crud(request):
	if request.method=="POST":
		un=request.POST['username']
		email=request.POST['email']
		pas=request.POST['pas']
		age=request.POST['age']
		if len(un)!=0:
			data=UsrRg.objects.create(username=un,password=pas,email=email,age=age)
			data2=UsrRg.objects.all()
			return render(request,'html/actions.html',{'info':data2})
			data2=UsrRg.objects.all()
	return render(request,'html/actions.html')

def deletedata(req,id):
	data=UsrRg.objects.get(id=id)
	data.delete()
	return render('/cr')







