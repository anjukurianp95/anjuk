from django.views.generic import TemplateView
from django.urls import path
from admapp import views
from student import views

urlpatterns=[
    path('',TemplateView.as_view(template_name='home.html'),name='home'),
    path('studentattendance',TemplateView.as_view(template_name='student-attendence.html'),name='student-attendence'),
    path('studentassessment',TemplateView.as_view(template_name='student-assessment.html'),name='student-assessment'),
    path('studentleavemanage',TemplateView.as_view(template_name='student-leave-management.html'),name='student-leave-management'),
    path('student-profile',TemplateView.as_view(template_name='student-profile.html'),name='student-profile'),
    path('studentpro',views.stupro,name='student-profile'),
    path('student-appliedleave',TemplateView.as_view(template_name='student-applied-leave.html'),name='student-applied-leave'),
    path('student-edit',TemplateView.as_view(template_name='student-edit.html'),name='student-edit'),
    path('studentedit',views.editstud,name='esave'),
    path('leaveapply',views.leaveapply,name='apply'),
    path('viewmarkstud',views.viewmarkstud,name='student-assessment'), 
    path('viewstudleave',views.viewstudleave,name='student-applied-leave'), 
     path('viewstudatte',views.viewstudatt,name='student-attendence'), 
]