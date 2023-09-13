from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib import messages

"""
    Use the LoginView class to create a login page.
    Use the LogoutView class to log a user out.
"""


class MyLoginView(LoginView):
    redirect_authenticated_user = True

    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse_lazy('tasks')

    def from_invalid(self, form):
        messages.error(self.request, 'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))


class MyLogoutView(LogoutView):
    template_name = 'users/logout.html'
    next_page = 'login'