from django.shortcuts import render, HttpResponseRedirect
from django.forms import ModelForm
from geeks.models import Todo

# Create your views here.
def index(request):
    context = {}
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = TodoForm()
    context['form'] = form
    return render(request, 'geeks/geeks.html', context)

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = "__all__"

