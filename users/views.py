from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import userRegisterForm,ProfileUpdateForm,UserUpdateForm
# Create your views here.

def register(request):
    if request.method =='POST':
        form = userRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request,f'Account created for {username}')
            return redirect('blog-home')
    else:
        form = userRegisterForm()
    return render(request,'users/register.html',context = {'form': form})


@login_required()
def profile(request):
    if request.method =='POST':
        p_update = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        u_update = UserUpdateForm(request.POST,instance=request.user)

        if (p_update.is_valid() and u_update.is_valid()):
            p_update.save()
            u_update.save()
            messages.success(request,f'your information is saved sucsessfully')
            return redirect('blog-home')


    else:
        p_update = ProfileUpdateForm(instance=request.user.profile)
        u_update = UserUpdateForm(instance=request.user)      
        

    context = {

        'p_update':p_update,
        'u_update':u_update,


    }

    return render(request,'users/profile.html',context=context)
    