import os
import csv
from app1.models import Job

def import_csv_to_database():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, 'app1', 'data', 'jobs_in_data.csv')

    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                Job.objects.create(
                    work_year=int(row['work_year']),
                    job_title=row['job_title'],
                    job_category=row['job_category'],
                    salary_currency=row['salary_currency'],
                    salary=float(row['salary']),
                    salary_in_usd=float(row['salary_in_usd']),
                    employee_residence=row['employee_residence'],
                    experience_level=row['experience_level'],
                    employment_type=row['employment_type'],
                    work_setting=row['work_setting'],
                    company_location=row['company_location'],
                    company_size=row['company_size']
                )
            except Exception as e:
                print(f"Error importing row: {row}. Error: {e}")
    print("Data imported successfully!")
