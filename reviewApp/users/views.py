from email import message
from multiprocessing import context
from re import template
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

def register(request):
    if request.method=='POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
            
        else: return redirect('about')

    else:
        form = UserRegisterForm()
        return render(request, 'users/register.html', {'form':form})

@login_required
def profile(request):
    if request.method =='POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid and p_form.is_valid:
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has sucessfully been updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        context = {
        'u_form' : u_form,
        'p_form' : p_form
        }

    return render(request, 'users/profile.html', context)

@login_required
def passwordChange(request):

    if request.method == 'POST':
        pform = PasswordChangeForm(request.user, request.POST)
        if pform.is_valid():
            user = pform.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password Changed Successfully')
            return redirect('profile')
        else:
            messages.error(request, 'Please fix error below')
            return render(request, 'users/passwordchange.html', context={'pform' : pform})
    else:
        pform = PasswordChangeForm(request.user)
    return render(request, 'users/passwordchange.html', context={'pform' : pform})


class PasswordReset(SuccessMessageMixin, PasswordResetView):
    template_name = 'users/passwordreset.html'
    success_message = "Password reset email sent!"
    success_url = '/login'
    email_template_name = 'users/passwordreset_email.html'
    subject_template_name = 'users/passwordreset_subject.txt'


# Create your views here.
