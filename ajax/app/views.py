# views.py
from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import UserApplication,UserProfile
from .forms import UserApplicationForm,RegistrationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login



@login_required
def apply(request):
    if request.method == 'POST':
        form = UserApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Application submitted successfully!'}, status=201)
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    return render(request, 'apply.html')

@login_required
def user_list_view(request):
    experience = request.GET.get('experience')
    job_role = request.GET.get('jobRole')

    users = UserApplication.objects.all()

    if experience:
        users = users.filter(experience__gte=experience)
    if job_role:
        users = users.filter(job_role__icontains=job_role)

    user_data = [{
        'name': user.name,
        'email': user.email,
        'experience': user.experience,
        'job_role': user.job_role,
        'resume': user.resume.url
    } for user in users]

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse(user_data, safe=False)


    return render(request, 'user_list.html', {'users': user_data})



def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user=form.save()
            UserProfile.objects.create(user=user)
            messages.success(request, 'Registration Success you can Login Now...!')
            return redirect('login')
    else:
        form= RegistrationForm()
    return render(request, 'register.html', {'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, 'Login successful!')

            if user.is_superuser:  
                return redirect('user_list') 
            else:
                return redirect('apply') 
        else:
            messages.error(request, 'Please enter a correct username and password. Note that both fields may be case-sensitive.')     
           
    else:
        form = AuthenticationForm()
        
    return render(request, 'login.html', {'form': form})
