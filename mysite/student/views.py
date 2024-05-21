from django.shortcuts import render, get_object_or_404
from .models import StudentDetail

def viewStudentList(request):
    students = StudentDetail.objects.all().order_by('first_name')
    return render(request, 'list.html', {'students': students})

def viewStudentDetails(request, student_id):
    student = get_object_or_404(StudentDetail, student_id=student_id)
    return render(request, 'detail.html', {'student': student})