from django.urls import path
from Emp import views

urlpatterns=[
    path('',views.home,name="hm"),
    path('abt/',views.about,name="ab"),
    path('con/',views.contactus,name="co"),
    path('lo/',views.login,name="log"),
    path('reg/',views.register,name="re"),
]