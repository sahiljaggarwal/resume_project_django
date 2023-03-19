from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    context = {'home':'active'}
    return render(request, 'core/home.html', context)

def contact(request):
    context = {'contact':'active'}
    return render(request, 'core/contact.html', context)

def projects(request):
    return redirect('https://github.com/sahiljaggarwal')

def hire(request):
    return redirect('https://www.linkedin.com/in/sahil-jaggarwal-1945881b3')

def twitter(request):
    return redirect('https://twitter.com/sahiljaggarwal?t=rxp7IKLlVbUr6Spb6jRI3Q&s=09')

def instagram(request):
    return redirect('https://instagram.com/sahiljaggarwal_?igshid=YmMyMTA2M2Y=')

def linkedin(request):
    return redirect('https://www.linkedin.com/in/sahil-jaggarwal-1945881b3')

def github(request):
    return redirect('https://github.com/sahiljaggarwal')