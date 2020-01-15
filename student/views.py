from django.shortcuts import render
from admapp.models import student,assessment,leave,attendance
from django.shortcuts import redirect
from admapp.models import leave
# Create your views here.

def stupro(request):
    queryset1=student.objects.filter(name=request.session['usr'])
    return render(request,'student-profile.html',{'r':queryset1})
def editstud(request):
    if request.method=="POST":
        stid=request.POST.get('stid')
        ano=request.POST.get('admissionno')
        name=request.POST.get('name')
        address=request.POST.get('address')
        dob=request.POST.get('dob')
        gender=request.POST.get('gender')
        qualification=request.POST.get('qualification')
        mobile=request.POST.get('mobile')
        batch=request.POST.get('batch')
        email=request.POST.get('email')
        password=request.POST.get('cpassword')
        adate=request.POST.get('adate')
        religion=request.POST.get('religion')
        blood=request.POST.get('blood')
        caste=request.POST.get('caste')
        student.objects.filter(name=request.session['usr']).update(address=address,gender=gender,caste=caste,qualification=qualification,mobile=mobile,email=email,religion=religion,blood=blood)
    return redirect('student-profile')

def leaveapply(request):
    if request.method=="POST":
        name=request.session['usr']
        ltype=request.POST.get('leavet')
        day=request.POST.get('day')
        date=request.POST.get('date')
        session=request.POST.getlist('session')
        reason=request.POST.get('reason')
        description=request.POST.get('description')
        a=leave(name=name,ltype=ltype,day=day,date=date,session=session,reason=reason,description=description)
        a.save()
    return redirect('student-leave-management')
    
def viewmarkstud(request):
    q=assessment.objects.all().filter(name=request.session['usr'])
    return render(request,'student-assessment.html',{'r':q})

def viewstudleave(request):
    q=leave.objects.all().filter(name=request.session['usr'])
    return render(request,'student-applied-leave.html',{'r':q})

def viewstudatt(request):
    q=attendance.objects.all().filter(name=request.session['usr'])
    return render(request,'student-attendence.html',{'r':q})



