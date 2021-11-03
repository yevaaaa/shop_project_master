from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from shop.forms import UserForm, NameForm
from django.http import HttpResponseRedirect


def home(request):
    return render(request,'shop/homepage.html')

def logout(request):
    return redirect('shop-register')


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'account created for {username}')
            return redirect('shop-homepage')
    else:
        form = UserForm()
        return render(request,'shop/register.html',{'form':form})

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance, populate it with data from the request:
        form = NameForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')
        else:
            form = NameForm()
            return render(request,'name.html', {'form':form})

def settings(request):
    return render(request,'shop/settings.html')