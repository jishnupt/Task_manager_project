from django import forms
from .models import CustomUser,Task
from django.contrib.auth.forms import UserCreationForm


class RegisteruserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username','email']

class TaskAddForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name','description','image']