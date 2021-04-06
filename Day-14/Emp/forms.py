from Emp.models import UsrRg
from django import forms

class UsregForm(forms.ModelForm):
	class Meta:
		model=UsrRg
		fields=['username','email','password']
		widgets={
		"username":forms.TextInput(attrs={"class":"form-control","placeholder":"enter username","required":True,}),
		"password":forms.PasswordInput(attrs={"class":"form-control","placeholder":"enter password","required":True,}),
		"email":forms.EmailInput(attrs={"class":"form-control","placeholder":"enter email","required":True,}),
		}

class Userupdate(forms.ModelForm):
	class Meta:
		model=UsrRg
		fields=['username','email','age']
		widgets={
		"username":forms.TextInput(attrs={"class":"form-control","placeholder":"enter username","required":True,}),
		"email":forms.EmailInput(attrs={"class":"form-control","placeholder":"enter email","required":True,}),
		"age":forms.NumberInput(attrs={"class":"form-control","placeholder":"update age","required":True,}),
		}
