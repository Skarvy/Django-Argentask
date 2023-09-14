from django.shortcuts import render,redirect, get_object_or_404
from .models import Task
from django.views import View
from .forms import UserForm, LoginForm
from django.contrib.auth.forms import UserCreationForm



# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    form = LoginForm
    return render(request, 'login.html',{
        'form' : form
    })




def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda los datos del usuario en la base de datos
            print("Datos capturados en el POST:", request.POST)  # Agrega un print para mostrar los datos
            return redirect('taskboard')  # Redirige a una página de éxito o a donde lo necesites
    else:
        form = UserForm()
    
    return render(request, 'register.html', {'form': form})

def taskboard(request):
    tasks = Task.objects.all()  # Recupera todas las tareas desde la base de datos
    print(tasks)
    return render(request, 'taskboard.html', {'tasks': tasks})




