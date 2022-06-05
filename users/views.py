from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

def register(request):
    
    if request.method == 'POST':

        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = User(username=username, email=email)
            user.set_password(password)
            user.save()
            messages.success(request, f'Your Account has beem created! ')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
   if request.method == 'POST':
       u_form = UserUpdateForm(instance=request.user)
       p_form = ProfileUpdateForm(request.POST, 
                                  request.FILES, 
                                  instance=request.user.profile)
       if u_form.is_valid() and p_form.is_valid():
           u_form.save()
           p_form.save()
           messages.success(request, f'Your Account has beem updated! ')
           return redirect('login')

   else:
       u_form = UserUpdateForm(instance=request.user)
       p_form = ProfileUpdateForm(instance=request.user.profile)

   context = {
        'u_form': u_form,
        'p_form': p_form
    }

   return render(request, 'users/profile.html', context)


