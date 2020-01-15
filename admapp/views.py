from django.shortcuts import render
from admapp.models import faculty,student,leave,assessment,attendance
from django.http import HttpResponse
from django.contrib.auth import logout
from django.shortcuts import redirect
# Create your views here.

def authentication(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        username=str(username)
        password=str(password)
        u=faculty.objects.filter(name=username,password=password)
        if(u.count()==1):
            request.session['usr']=username
            return render(request,'faculty-login.html')
        else:
            u1=student.objects.filter(name=username,password=password)
            if(u1.count()==1):
                request.session['usr']=username
                return render(request,'home.html')
            else:
                return HttpResponse('Username or Password incorrect')

def proffac(request):
    queryset1=faculty.objects.filter(name=request.session['usr'])
    return render(request,'faculty-profile.html',{'r':queryset1})

def proffacedit(request):
    if request.method=="POST":
        name=request.POST.get('name')
        address=request.POST.get('address')
        dob=request.POST.get('dob')
        gender=request.POST.get('gender')
        qualification=request.POST.get('qualification')
        mobile=request.POST.get('mobile')
        batch=request.POST.get('batch')
        email=request.POST.get('email')
        password=request.POST.get('cpassword')
        jdate=request.POST.get('jdate')
        designation=request.POST.get('designation')
        blood=request.POST.get('blood')
        faculty.objects.filter(name=request.session['usr']).update(name=name,address=address,gender=gender,qualification=qualification,batchincharge=batch,mobile=mobile,email=email,password=password,blood=blood,designation=designation)
    return redirect('faculty-profile')

def viewleave(request):
    queryset1=leave.objects.all()
    return render(request,'student-leave.html',{'r':queryset1})

def approveleave(request):
    if request.method=='POST':
        name=request.POST.get('name')
        leave.objects.filter(name=name).update(status='Approved')
        return redirect('student-leave')

def assess(request):
    if request.method=='POST':
        name=request.POST.get('name')
        asno=request.POST.get('asno')
        date=request.POST.get('date')
        mark1=request.POST.get('mark1')
        mark2=request.POST.get('mark2')
        mark3=request.POST.get('mark3')
        total=request.POST.get('total')
    b=assessment(name=name,asno=asno,date=date,mark1=mark1,mark2=mark2,mark3=mark3,total=total)
    b.save()
    return redirect('assessment')

def viewmark(request):
    queryset1=assessment.objects.all()
    return render(request,'assessment.html',{'r':queryset1})
   
def addattendance(request):
    if request.method=="POST":
        name=request.session['usr']
        date=request.POST.get('date')
        h1=request.POST.get('h1')
        h2=request.POST.get('h2')
        h3=request.POST.get('h3')
        h4=request.POST.get('h4')
        c=attendance(name=name,date=date,status1=h1,status2=h2,status3=h3,status4=h4)
        c.save()
    return redirect('attendence_1')
