from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('',views.index,name="home"),
    path('about',views.AboutUs,name="about"),
    path('contact',views.ContactUs,name="contact"),
    path('searchjob',views.SearchJob,name="searchjob"),
    path('studyabroad',views.StudyAbroad,name="studyabroad"),
    path('login',views.LoginUser,name="login"),
    path('logout',views.LogoutUser,name="logout"),
    path('signup',views.SignupUser,name="signup"),
    path("skill-assessment/", views.skill_assessment, name="skill_assessment"),
    path("fulltime_job", views.FullTimeJobs, name="fulltime_Jobs"),
    path("parttime_job", views.PartTimeJobs, name="parttime_Job"),
    path("internship", views.Internship, name="Internships"),
    path("job/<int:job_id>/", views.JobDetails, name="jobdetails"),
    path("progresstracking", views.ProgressTrack, name="progresstrack"),
    path("contactus", views.ContactUs, name="contactus"),
    path("aboutus", views.AboutUs, name="aboutus"),
    path("community", views.Community, name="community"),
    path("blogs", views.Blogs, name="blogs"),
    path("faqs", views.Faqs, name="faqs"),
    path("upload_resume", views.Upload_resume, name="upload_resume"),
    # path('SignupUser',views.SignupUser,"Signup"),
]