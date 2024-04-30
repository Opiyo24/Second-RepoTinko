from django.shortcuts import render
from django import forms

# Create your views here.
def index(request):
    context = {}
    context['form'] = InputForm()
    return render(request, "forms/index.html", context)

class GeeksForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()


class InputForm(forms.Form):
    first_name = forms.CharField(max_length = 200)
    last_name = forms.CharField(max_length = 200)
    roll_numner = forms.IntegerField(help_text = "Enter 6 digit roll number")
    password = forms.CharField(widget = forms.PasswordInput())

