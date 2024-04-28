from django import forms
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Player

# Create your views here.
def home(request):
    form = PlayerForm()
    context = {
        "form": form
    }
    return render(request, 'blackjack/index.html', context)

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = "__all__"


def create_player(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
