from django.db import models

# Create your models here.

class Job(models.Model):
    work_year = models.IntegerField()
    job_title = models.CharField(max_length=255)
    job_category = models.CharField(max_length=100, choices=[('IT', 'IT'), ('Finance', 'Finance'), ('Healthcare', 'Healthcare')])
    salary_currency = models.CharField(max_length=10)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    salary_in_usd = models.DecimalField(max_digits=10, decimal_places=2)
    employee_residence = models.CharField(max_length=100)
    experience_level = models.CharField(
        max_length=50,
        choices=[('Junior', 'Junior'), ('Mid', 'Mid'), ('Senior', 'Senior'), ('Executive', 'Executive')]
    )
    employment_type = models.CharField(
        max_length=50,
        choices=[('Full-time', 'Full-time'), ('Part-time', 'Part-time'), ('Contract', 'Contract'),('Internship', 'Internship')]
    )
    work_setting = models.CharField(
        max_length=50,
        choices=[('Remote', 'Remote'), ('On-site', 'On-site'), ('Hybrid', 'Hybrid')]
    )
    company_location = models.CharField(max_length=100)
    company_size = models.CharField(
        max_length=50,
        choices=[('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large')]
    )

    def __str__(self):
        return f"{self.job_title} at {self.company_location}"