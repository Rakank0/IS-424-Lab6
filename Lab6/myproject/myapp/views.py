from django.shortcuts import render,redirect
from .models import Student, Course
from .forms import StudentForm, CourseForm,CourseSelectionForm

# Create your views here.
def students_view(request):
    students = Student.objects.all()
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('students')
    return render(request, 'students.html', {'students': students, 'form': form})

def courses_view(request):
    courses = Course.objects.all()
    form = CourseForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('courses')
    return render(request, 'courses.html', {'courses': courses, 'form': form})


def details_view(request, student_id):
    student = Student.objects.get(id=student_id)
    not_registered_courses = Course.objects.exclude(students=student)
    
    if request.method == 'POST':
        form = CourseSelectionForm(request.POST)
        if form.is_valid():
            selected_courses = form.cleaned_data['courses']
            student.courses.add(*selected_courses)
            return redirect('details', student_id=student_id)
    else:
        form = CourseSelectionForm()

    return render(request, 'details.html', {'student': student, 'not_registered_courses': not_registered_courses, 'form': form})


