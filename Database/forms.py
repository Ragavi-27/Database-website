from django import forms
from django.views.decorators.csrf import csrf_exempt
from Database.models import EmpModel
@csrf_exempt

class Empforms(forms.ModelForm):
    class Meta:
        model=EmpModel
        fields="__all__"
        

class Deptforms(forms.ModelForm):
    class Meta:
        model=Empdept
        fields="__all__"
