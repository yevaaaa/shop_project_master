from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from users.forms import UserForm, NameForm, ContactusForm
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
        return render(request,'users/register.html',{'form':form})

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
            return render(request,'user/name.html', {'form':form})



def contact(request):
    if request.method == 'POST':
        form = ContactusForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            message = form.cleaned_data.get('message')

            subject = 'Someone contacted us'
            content = f"""
            {first_name} {last_name} is trying to contact u .
            Their email address is: {email}
            Message: {message}
            """

            send_mail(subject=subject, message=content,
                      from_email='shopforproject@gmail.com',
                      recipient_list=['shopforproject@gmail.com'])
            return redirect('thank_you')

    else:
        form = ContactusForm()

    return render(request, 'users/contact_us.html', {'form': form})

def thank_you(request):
    return render(request, 'users/thank_you.html' )

def contact(request):
    if request.method == 'POST':
        form = ContactusForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            message = form.cleaned_data.get('message')

            subject = 'Someone contacted us'
            content = f"""
            {first_name} {last_name} is trying to contact u .
            Their email address is: {email}
            Message: {message}
            """

            send_mail(subject=subject, message=content,
                      from_email='test.basic90@gmail.com',
                      recipient_list=['test.basic90@gmail.com'])
            return redirect('thank_you')

















# Create your views here.
