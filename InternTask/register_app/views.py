from django.shortcuts import render
from register_app.forms import UserForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, 'register_app/index.html')

def register(request):

    registered = False

    if request.method == 'POST':

        user_form = UserForm(data=request.POST)

        if user_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            registered = True

        else:
            print(user_form.errors)
    else:
        user_form = UserForm()

    return render(request, 'register_app/registeration.html', {'registered': registered,
                                                                'user_form': user_form})


def user_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                print('User Not Active')
        else:
            return HttpResponse('Invalid Login Details. If you have not registered yet. Register first.')
    else:
        return render(request, 'register_app/login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponse('<div class="jumbotron"> <h1> Logged Out </h1>')
