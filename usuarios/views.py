from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . import forms


# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('proyecto:general')
    else:
        if request.user.is_authenticated:
            return redirect('proyecto:general')
        else:
            form = AuthenticationForm(request)
            form.fields['username'].widget.attrs['class'] = "form-control"
            form.fields['password'].widget.attrs['class'] = "form-control"
    return render(request,'usuarios/login.html',{'form':form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect("usuario:login")

def add_user(request):
    if request.method == 'POST':
        form = forms.AgregarForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=raw_password)
            return redirect('proyecto:general')
    else:
        form = forms.AgregarForm()
    return render(request,'usuarios/agregar-usuario.html',{'form':form})
