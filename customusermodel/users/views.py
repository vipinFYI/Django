from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .forms import CustomUserCreationForm

# Create your views here.

#class bases view

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
 

# def SignUpView(req):
#     form = CustomUserCreationForm
#     if req.method == 'POST':
#         form = CustomUserCreationForm(req.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     return render(req, 'signup.html', {'form': form})