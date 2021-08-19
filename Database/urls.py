from django.contrib import admin
from django.urls import path
from Database import views
from . import views

urlpatterns = [
    path('',views.Homedb,name="HomeEmp"),
    path("ShowEmp", views.showEmp, name="showemp"),
    path('AddEmployee',views.InsertEmp,name="Insertemp"),
    path('edit/<int:id>',views.EditEmp,name="Editemp"),
    path('Update/<int:id>',views.UpdateEmp,name='UpdateEmp'),
    path('Delete/<int:id>',views.DelEmp,name='DelEmp'),
    path('Department',views.showDept,name='showDept'),
    path('AddDepartment',views.InsertDept,name='InsertDept'),
    path('edit_dept/<int:id>',views.Editdept,name="Editdept"),
    path('Delete_dept/<int:id>',views.Deldept,name='Deldept'),
    path('Update_dept/<int:id>',views.UpdateEmp,name='UpdateEmp'),
]
