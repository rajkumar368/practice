from django.shortcuts import render,redirect,HttpResponse
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import auth
from django.contrib import auth
from account.models import Patient,Doctor,Clinic_admin

# Create your views here.

def patient_signup(request):
    if request.method == 'POST':
        if request.POST["pwd1"] == request.POST["pwd2"]:
            try:
                user=User.objects.get(username=request.POST['uname'])
                return render(request,'patient/signup.html')
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['uname'],password=request.POST['pwd1'])
                name = request.POST['name']
                email = request.POST['email']
                pat_obj = Patient(user_id=user.id,name= name,email=email )
                pat_obj.save()
                auth.login(request,user)
                return redirect("logins")
        else:
            return render(request,'patient/signup.html')

    return render(request,'patient/signup.html')


def doctor_signup(request):
    if request.method == 'POST':
        if request.POST["pwd1"] == request.POST["pwd2"]:
            try:
                user=User.objects.get(username=request.POST['uname'])
                return render(request,'doctor/signup.html')
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['uname'],password=request.POST['pwd1'])
                name = request.POST['name']
                email = request.POST['email']
                cname = request.POST['cname']
                doc_obj = Doctor(user_id=user.id,name= name,email=email,clinic_name=cname)
                doc_obj.save()
                auth.login(request,user)
                return redirect("logins")
        else:
            return render(request,'doctor/signup.html')

    return render(request,'doctor/signup.html')

def clinic_admin_signup(request):
    if request.method == 'POST':
        if request.POST["pwd1"] == request.POST["pwd2"]:
            try:
                user=User.objects.get(username=request.POST['uname'])
                return render(request,'clinic_admin/signup.html')
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['uname'],password=request.POST['pwd1'])
                name = request.POST['name']
                email = request.POST['email']
                cname = request.POST['cname']
                mobile = request.POST['mobile']
                ca_obj = Clinic_admin(user_id=user.id,name= name,email=email,clinic_name=cname,mobile=mobile )
                ca_obj.save()
                auth.login(request,user)
                return redirect("logins")
        else:
            return render(request,'clinic_admin/signup.html')

    return render(request,'clinic_admin/signup.html')


def logins(request):
    if request.method == "POST":
        username = request.POST['uname']
        password = request.POST['pwd']
        usr = auth.authenticate(username=username,password=password)
        if usr is not None:
            auth.login(request,usr)
            try:
                if Patient.objects.filter(user = usr):
                    return render(request,'patient/p_dashboard.html')       
                elif Doctor.objects.filter(user = usr):
                    return render(request,'doctor/d_dashboard.html')
                else:
                    return render(request,'clinic_admin/c_dashboard.html')
            except:
                pass
        else:
            return render(request,'login.html')
    
    return render(request,'login.html')
