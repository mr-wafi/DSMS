from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from app.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from app.models import Course, CustomUser, Session_Year, Student
from django.contrib.auth.decorators import login_required


def BASE(request):
    return render(request, 'base.html')


def Login(request):
    return render(request, 'login.html')


def doLogin(request):
    if request.method == "POST":
        user = EmailBackEnd.authenticate(request,
                                         username=request.POST.get('email'),
                                         password=request.POST.get('password'),
                                         )

        if user != None:
            login(request, user)  # type: ignore
            user_type = user.user_type  # type: ignore
            if user_type == '1':
                messages.success(request, 'Hod Logged In Successfully!!')
                return redirect('Hod_home')
            elif user_type == '2':
                messages.success(request, 'Staff Logged In Successfully!!')
                return redirect('staff_home')

            elif user_type == '3':
                messages.success(request, 'Student Logged In Successfully!!')
                return redirect('student_home')

            else:
                messages.error(request, f'Check credentials')
                return redirect('Login')
        else:
            messages.error(request, f'Incorrect username')
            return redirect('Login')


def doLogout(request):
    logout(request)
    return redirect('Login')


@login_required(login_url='/')
def PROFILE(request):
    user = CustomUser.objects.get(id=request.user.id)
    context = {
        'user': user
    }
    return render(request, 'profile.html', context)


@login_required(login_url='/')
def PROFILE_UPDATE(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']

        try:
            customuser = CustomUser.objects.get(pk=request.user.id)
            customuser.first_name = first_name
            customuser.last_name = last_name
            if password != None and password != '':
                customuser.set_password(password)

            if profile_pic != None and profile_pic != '':
                customuser.profile_pic = profile_pic

            customuser.save()
            messages.success(request, f'Profile Updated Successfully!!')
            return redirect('profile')
        except:
            messages.warning(
                request, 'Profile dose not updated successfully!!')
    return render(request, 'profile.html')
