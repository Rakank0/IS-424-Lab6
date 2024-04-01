from django import forms
from .models import Course

class CourseSelectionForm(forms.Form):
    courses = forms.ModelMultipleChoiceField(queryset=Course.objects.all(), widget=forms.CheckboxSelectMultiple)
