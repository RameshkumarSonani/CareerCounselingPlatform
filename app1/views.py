# views.py
from django.shortcuts import render, HttpResponse , redirect,get_object_or_404
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.models import User
from django.contrib import messages
from .questions import QUESTIONS 
from django.db.models import Q
from .models import Job
# uploading Resume
from .models import Resume


def index(request):
    if request.user.is_anonymous:
       return render(request,"login.html")
    return render(request, "index.html")

def AboutUs(request):
    return render(request, "aboutus.html")

def Community(request):
    return render(request, "community.html")

def ContactUs(request):
    return render(request, "contactus.html")

def SearchJob(request):
    return render(request, "serachjob.html")

def StudyAbroad(request):
    return render(request, "studyabroad.html")

def Blogs(request):
    return render(request, "blogs.html")
def Faqs(request):
    return render(request, "faqs.html")

def LoginUser(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username=username, password=password)
        print(username,password)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            messages.warning(request, "Enter The Right Details Of Account..")
            redirect("/login")
    return render(request,'login.html')

def SignupUser(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password')
        pass2=request.POST.get('confirmPassword')
        if pass1!=pass2:
            messages.warning(request, "Your Password Did Not Match To Confirm-Password..")
            # return HttpResponse("password did not match with confirm pass")
        else:
            my_user= User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect("/login")
            # return HttpResponse("User has been created ")
    return render(request,'signup.html')

def FullTimeJobs(request):
    # Retrieve filters from the request
    location = request.GET.get('location', '')
    salary_min = request.GET.get('salary_min')
    salary_max = request.GET.get('salary_max')

    # Convert salary range to integers or set default values
    try:
        salary_min = float(salary_min) if salary_min else 0  # Minimum salary default is 0
        salary_max = float(salary_max) if salary_max else 1_000_000  # Set a high realistic maximum
    except ValueError:
        salary_min, salary_max = 0, 1_000_000

    # Filter jobs based on the inputs
    jobs = Job.objects.filter(employment_type='Full-time')

    if location:
        jobs = jobs.filter(company_location=location)
    jobs = jobs.filter(salary_in_usd__gte=salary_min, salary_in_usd__lte=salary_max)

    # Get unique locations for filter dropdown
    locations = Job.objects.values_list('company_location', flat=True).distinct()

    return render(request, 'fulltime_job.html', {'jobs': jobs, 'locations': locations})



def PartTimeJobs(request):
    location = request.GET.get('location', '')
    salary_min = request.GET.get('salary_min')
    salary_max = request.GET.get('salary_max')

    # Convert salary range to integers or set default values
    try:
        salary_min = float(salary_min) if salary_min else 0  # Minimum salary default is 0
        salary_max = float(salary_max) if salary_max else 1_000_000  # Set a high realistic maximum
    except ValueError:
        salary_min, salary_max = 0, 1_000_000

    # Filter jobs based on the inputs
    jobs = Job.objects.filter(employment_type='Part-time')

    if location:
        jobs = jobs.filter(company_location=location)
    jobs = jobs.filter(salary_in_usd__gte=salary_min, salary_in_usd__lte=salary_max)

    # Get unique locations for filter dropdown
    locations = Job.objects.values_list('company_location', flat=True).distinct()

    return render(request, 'parttime_job.html', {'jobs': jobs, 'locations': locations})

def JobDetails(request, job_id):
    job = get_object_or_404(Job, id=job_id)  # Specific job fetch karein
    print(job)
    return render(request, 'jobdetails.html', {'job': job})

def Internship(request):
    location = request.GET.get('location', '')
    salary_min = request.GET.get('salary_min')
    salary_max = request.GET.get('salary_max')

    # Convert salary range to integers or set default values
    try:
        salary_min = float(salary_min) if salary_min else 0  # Minimum salary default is 0
        salary_max = float(salary_max) if salary_max else 1_000_000  # Set a high realistic maximum
    except ValueError:
        salary_min, salary_max = 0, 1_000_000

    # Filter jobs based on the inputs
    jobs = Job.objects.filter(employment_type='Internship')

    if location:
        jobs = jobs.filter(company_location=location)
    jobs = jobs.filter(salary_in_usd__gte=salary_min, salary_in_usd__lte=salary_max)

    # Get unique locations for filter dropdown
    locations = Job.objects.values_list('company_location', flat=True).distinct()

    print()
    return render(request, 'internship.html', {'jobs': jobs, 'locations': locations})

def LogoutUser(request):
    logout(request)
    return render(request,"login.html")

def skill_assessment(request):
    if request.method == "POST":
        # Step 1: Agar user ne questions submit kiye hain
        if "question_1" in request.POST:
            skill_category = request.POST.get('skill_category').lower()
            skill_level = request.POST.get('skill_level').lower()
            questions = QUESTIONS.get(skill_category, {}).get(skill_level, [])
            
            # Check and calculate score
            correct_count = 0
            user_answers = {}

            for i, question in enumerate(questions, start=1):
                user_answer = request.POST.get(f"question_{i}")
                correct_answer = question["correct"]

                user_answers[question["text"]] = {
                    "user_answer": user_answer,
                    "correct_answer": correct_answer,
                    "is_correct": user_answer == correct_answer
                }

                if user_answer == correct_answer:
                    correct_count += 1

            # Calculate score
            total_questions = len(questions)
            score = (correct_count / total_questions) * 100 if total_questions else 0

            # Pass results to template
            context = {
                "skill_category": skill_category,
                "skill_level": skill_level,
                "score": score,
                "user_answers": user_answers
            }
            return render(request, "result.html", context)

        # Agar skill category/level select hai, to questions dikhayein
        elif "skill_category" in request.POST:
            skill_category = request.POST.get('skill_category').lower()
            skill_level = request.POST.get('skill_level').lower()
            questions = QUESTIONS.get(skill_category, {}).get(skill_level, [])
            
            if not questions:
                    return HttpResponse(f"No questions available for the category '{skill_category}' and level '{skill_level}'.")

            context = {
                "skill_category": skill_category,
                "skill_level": skill_level,
                "questions": questions,
            }
            return render(request, "questions.html", context)

    # Default: Skill Assessment Form dikhaana
    return render(request, "skill-assessment.html")

def ProgressTrack(request):
    return render(request,"progresstracking.html")

# Uloading Resume
def Upload_resume(request):
    if request.method == "POST" and request.FILES.get('resume'):
        resume_file = request.FILES['resume']
        resume_instance, created = Resume.objects.get_or_create(user=request.user)
        resume_instance.resume = resume_file
        resume_instance.save()
        return HttpResponse("Your resume has been successfully uploaded!")  # Replace with actual success page
    return render(request, "upload_resume.html")

def success_page(request):
    return render(request, 'success.html')