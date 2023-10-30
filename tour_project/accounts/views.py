from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy

from .forms import UserRegistrationForm, UserEditForm


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            login(request, authenticate(username=new_user.username, password=user_form.cleaned_data['password']))
            return redirect('services:services_list')
        else:
            messages.error(request, "Registration error. Please check your credentials and try again.")
    else:
        user_form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'user_form': user_form})



class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True

    def form_invalid(self, form):
        messages.error(self.request, "Login error. Please check your credentials and try again.")
        return super().form_invalid(form)

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('services:services_list')

class UserProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'accounts/user_profile.html'
    context_object_name = 'user'

    def get_object(self):
        return self.request.user

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserEditForm
    template_name = 'accounts/update_profile.html'
    success_url = reverse_lazy('accounts:user_profile')

    def get_object(self):
        return self.request.user

class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'accounts/delete_profile.html'
    success_url = reverse_lazy('services:services_list')
    confirmation_required = True

    def get_object(self):
        return self.request.user
