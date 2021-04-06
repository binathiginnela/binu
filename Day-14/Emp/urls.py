from django.urls import path
from Emp import views

urlpatterns=[
    path('',views.home,name="hm"),
    path('abt/',views.about,name="ab"),
    path('con/',views.contactus,name="co"),
    path('lo/',views.login,name="log"),
    path('reg/',views.register,name="re"),
    path('cr/',views.crud,name="cd"),
    path('del/<int:id>',views.deletedata,name="delete"),
    path('df/',views.dform,name="dff"),
    path('sh/',views.showinfo,name="show"),
    path('infodelete/<int:id>',views.infodelete,name="infodelete"),
    # path('edit/<int:id>',views.edit,name="editdata"),
    path('e/<int:si>/',views.userupdate,name="ue"),
]