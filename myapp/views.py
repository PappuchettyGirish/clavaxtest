from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from myapp.models import Userdata
from .forms import UserForm,LoginForm
from django.views.generic import ListView


def index(request):
    return HttpResponse("<h1>Working Girish</h1>")


def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST,request.FILES)
        if form.is_valid():
            name=form.cleaned_data['name']
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            address=form.cleaned_data['address']
            image=form.cleaned_data['image']
            user=Userdata(name=name,username=username,email=email,password=password,address=address,image=image)
            user.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/login/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserForm()

    return render(request, 'myapp/signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            request.session['username'] = username
            password=form.cleaned_data['password']
            return HttpResponseRedirect('/user/',{'username':username})
        else:
            return HttpResponse("Username or password are not matching. Please try again")
    else:
        form=LoginForm()
        return render(request, 'myapp/login.html', {'form': form})

def user(request):
    if (request.session.has_key('username')):
        uname=request.session['username']
        user=Userdata.objects.filter(username=uname)
        return render(request, 'myapp/user.html', {'user': user,'uname':uname})

class MemberList(ListView):
    model=Userdata

def logout(request):
    try:
        del request.session['username']
        return HttpResponseRedirect('/login/')
    except KeyError:
        pass
        return render(request, 'myapp/index.html',{})
