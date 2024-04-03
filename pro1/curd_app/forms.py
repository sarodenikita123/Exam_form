from django import forms
from .models import Exam


class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = "__all__"

        widgets = {
            "student_name": forms.TextInput(attrs={"class": "form-control"}),
            "register_number": forms.NumberInput(),
            "register_course": forms.TextInput(attrs={"class": "form-control"}),
            "gender": forms.RadioSelect(),
            "exam_start": forms.DateInput(),
            "exam_end": forms.DateInput()
        }
