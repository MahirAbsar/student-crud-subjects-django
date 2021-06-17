from django.shortcuts import render
from django.http import HttpResponse
from .models import Student,Subject
from first_app import forms
# Create your views here.


def index(request):
    all_students = Student.objects.order_by("-cgpa")
    diction = {"all_students":all_students}
    return render(request,"first_app/index.html",context=diction)

def add_student(request):
    student_form = forms.StudentForm()
    diction = {"title":"Enlist_Student","student_form":student_form}

    if request.method=="POST":
        student_form = forms.StudentForm(request.POST)
        if student_form.is_valid():
            student_form.save()
            return index(request)

    return render(request,"first_app/add_student.html",context=diction)

def add_subject(request):
    subject_form = forms.SubjectForm()
    diction = {"title":"Add Subject","subject_form":subject_form}

    if request.method == "POST":
        subject_form = forms.SubjectForm(request.POST)
        if subject_form.is_valid():
            subject_form.save()
            return index(request)
    return render(request,"first_app/add_subject.html",context=diction)

def student_detail(request,id):
    get_student = Student.objects.get(pk=id)
    get_subject = Subject.objects.filter(student=id).order_by('-difficulty_level')
    diction = {"title":"Student Info","student_info":get_student,"subjects":get_subject}
    return render(request,"first_app/student_info.html",context=diction)

def edit_info_student(request,id):
    get_student = Student.objects.get(pk=id)
    student_form = forms.StudentForm(instance=get_student)
    if request.method=="POST":
        student_form = forms.StudentForm(request.POST,instance=get_student)
        if student_form.is_valid():
            student_form.save()
            return student_detail(request,id)

    diction = {'student_form':student_form,"title":"Edit Info","student_edit":True}
    return render(request,"first_app/edit_page.html",context=diction)

def edit_info_subject(request,id):
    get_subject = Subject.objects.get(pk=id)
    subject_form = forms.SubjectForm(instance=get_subject)
    diction ={"updated":False}
    if request.method=="POST":
        subject_form = forms.SubjectForm(request.POST,instance=get_subject)
        if subject_form.is_valid():
            subject_form.save()
            diction.update({"updated":True})
    diction.update({"title":"Edit"})
    diction.update({"subject_form":subject_form})
    diction.update({"id":id})
    return render(request,"first_app/edit_page.html",context=diction)

def delete_subject(request,id):
    delete_subject = Subject.objects.get(pk=id).delete()
    diction = {"message":"Deleted successfully"}
    return render(request,"first_app/delete_info.html",context=diction)

def delete_student(request,id):
    delete_student = Student.objects.get(pk=id).delete()
    diction = {"message":"Deleted successfully"}
    return render(request,"first_app/delete_info.html",context=diction)
