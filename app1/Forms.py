from django import forms
from .models import Resume

class ResumeUploadForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['resume']

    def clean_resume(self):
        resume = self.cleaned_data.get('resume')
        if resume:
            if resume.size > 2 * 1024 * 1024:  # 2MB limit
                raise forms.ValidationError("File size should not exceed 2MB.")
        return resume
