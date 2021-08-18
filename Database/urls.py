from django.urls import path
from Database import views

urlpatterns = [
    path('',views.Homedb,name="HomeEmp"),
    path("ShowEmp", views.showEmp, name="showemp"),
    path('AddEmployee',views.InsertEmp,name="Insertemp"),
]