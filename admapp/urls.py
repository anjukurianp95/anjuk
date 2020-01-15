from django.views.generic import TemplateView
from django.urls import path
from admapp import views

urlpatterns=[
    path('',TemplateView.as_view(template_name='index.html'),name='index'),
    path('login/',TemplateView.as_view(template_name='login.html'),name='login'),
    path('faclogin/',TemplateView.as_view(template_name='faculty-login.html'),name='faculty-login'),
    path('signin',views.authentication,name='signin'),
    path('student-leave/',TemplateView.as_view(template_name='student-leave.html'),name='student-leave'),
    path('studentleave',views.viewleave,name='student-leave'),
    path('leaveapprove',views.approveleave,name='approve'),
    path('assessment/',TemplateView.as_view(template_name='assessment.html'),name='assessment'),
    path('attendence_1/',TemplateView.as_view(template_name='attendence_1.html'),name='attendence_1'),
    path('faclogin/',TemplateView.as_view(template_name='faculty-login.html'),name='faclogin'),
    path('facprofile/',TemplateView.as_view(template_name='faculty-profile.html'),name='faculty-profile'),
    path('facultyprofile',views.proffac,name='faculty-profile'),
    path('facprofileedit/',TemplateView.as_view(template_name='faculty-profile-edit.html'),name='faculty-profile-edit'),
    path('facultyprofileedit',views.proffacedit,name='sbm'),
    path('leave-forwarded/',TemplateView.as_view(template_name='leave-forwarded.html'),name='leave-forwarded'),
    path('leave-rejected/',TemplateView.as_view(template_name='leave-rejected.html'),name='leave-rejected'),
    path('charts/',TemplateView.as_view(template_name='charts.html'),name='charts'),
    path('addmarks',views.assess,name='create'),
    path('viewmark',views.viewmark,name='assessment'), 
    path('addatten',views.addattendance,name='sbm'), 
]