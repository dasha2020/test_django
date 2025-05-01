from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from albums.models import Student, Teacher, Subject, Class
import xlsxwriter
from django.contrib import messages
from django.db import IntegrityError
from django.views.generic.base import TemplateView, View
from django.views.generic.edit import FormView
from django.urls import reverse, reverse_lazy
from .forms import StudentForm, StudentDeleteForm, TeacherForm, TeacherDeleteForm, SubjectForm, SubjectDeleteForm, ClassForm, ClassDeleteForm, LoginForm, CustomUserCreationForm, ForgotForm, ChangeForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from albums.services.email_service import ForgotPassView
import smtplib
from email.mime.text import MIMEText
import random
import string

me = 'dariia.d57@gmail.com'
you = 'user@example.com'
password = 'rwbk cvsv zvpv ajzk'

# Create your views here.

grades = Class.objects.all()
subjects = Subject.objects.all()


class StudentFormView(FormView):
    template_name = "add_student.html"
    form_class = StudentForm
    success_url = "/students_main/"

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        age = form.cleaned_data['age']
        grade = form.cleaned_data['grade']
        grade = Class.objects.get(grade=grade)

        Student.objects.create(
            first_name=first_name,
            last_name=last_name,
            age=age,
            grade=grade
        )
        return super().form_valid(form)

class StudentManageFormView(LoginRequiredMixin, FormView):
    form_class = StudentForm
    success_url = "/students_main/"

    def dispatch(self, request, *args, **kwargs):
        self.student_id = kwargs.get('student_id')
        self.student = None
        if self.student_id:
            self.student = Student.objects.get(id=self.student_id)
        return super().dispatch(request, *args, **kwargs)

    def get_template_names(self):
        if self.student:
            return ["edit_student.html"]
        return ["add_student.html"]

    def get_initial(self):
        if self.student:
            return {
                'first_name': self.student.first_name,
                'last_name': self.student.last_name,
                'age': self.student.age,
                'grade': self.student.grade,
            }
        return super().get_initial()

    def form_valid(self, form):
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        age = form.cleaned_data['age']
        grade = form.cleaned_data['grade']
        grade = Class.objects.get(grade=grade)

        if self.student:
            self.student.first_name = first_name
            self.student.last_name = last_name
            self.student.age = age
            self.student.grade = grade
            self.student.save()
        else:
            Student.objects.create(
                first_name=first_name,
                last_name=last_name,
                age=age,
                grade=grade
            )

        return super().form_valid(form)


class StudentDeleteFormView(LoginRequiredMixin, FormView):
    form_class = StudentDeleteForm
    template_name = "delete_student.html"
    success_url = "/delete_list_student/"

    def dispatch(self, request, *args, **kwargs):
        self.student_id = kwargs.get('student_id')
        self.student = None
        if self.student_id:
            self.student = Student.objects.get(id=self.student_id)
        return super().dispatch(request, *args, **kwargs)

    def get_initial(self):
        if self.student:
            return {
                'first_name': self.student.first_name,
                'last_name': self.student.last_name,
                'age': self.student.age,
                'grade': self.student.grade,
            }
        return super().get_initial()

    def form_valid(self, form):
        self.student.delete()

        return super().form_valid(form)

class TeacherManageFormView(LoginRequiredMixin, FormView):
    form_class = TeacherForm
    success_url = "/teachers_main/"

    def dispatch(self, request, *args, **kwargs):
        self.teacher_id = kwargs.get('teacher_id')
        self.teacher = None
        if self.teacher_id:
            self.teacher = Student.objects.get(id=self.teacher_id)
        return super().dispatch(request, *args, **kwargs)

    def get_template_names(self):
        if self.teacher:
            return ["edit_teacher.html"]
        return ["add_teacher.html"]

    def get_initial(self):
        if self.teacher:
            return {
                'first_name': self.teacher.first_name,
                'last_name': self.teacher.last_name,
                'age': self.teacher.age,
                'grade': self.teacher.grade,
            }
        return super().get_initial()

    def form_valid(self, form):
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        subject = form.cleaned_data['subject']
        subject = Subject.objects.get(name=subject)

        if self.teacher:
            self.teacher.first_name = first_name
            self.teacher.last_name = last_name
            self.teacher.subject = subject
            self.teacher.save()
        else:
            Teacher.objects.create(
                first_name=first_name,
                last_name=last_name,
                subject=subject
            )

        return super().form_valid(form)


class TeacherDeleteFormView(LoginRequiredMixin, FormView):
    form_class = StudentDeleteForm
    template_name = "delete_teacher.html"
    success_url = "/delete_list_teacher/"

    def dispatch(self, request, *args, **kwargs):
        self.teacher_id = kwargs.get('teacher_id')
        self.teacher = None
        if self.teacher_id:
            self.teacher = Teacher.objects.get(id=self.teacher_id)
        return super().dispatch(request, *args, **kwargs)

    def get_initial(self):
        if self.teacher:
            return {
                'first_name': self.teacher.first_name,
                'last_name': self.teacher.last_name,
                'subject': self.teacher.subject,
            }
        return super().get_initial()

    def form_valid(self, form):
        self.teacher.delete()

        return super().form_valid(form)
    

class SubjectManageFormView(LoginRequiredMixin, FormView):
    form_class = SubjectForm
    success_url = "/subjects_main/"

    def dispatch(self, request, *args, **kwargs):
        self.subject_id = kwargs.get('subject_id')
        self.subject = None
        if self.subject_id:
            self.subject = Subject.objects.get(id=self.subject_id)
        return super().dispatch(request, *args, **kwargs)

    def get_template_names(self):
        if self.subject:
            return ["edit_subject.html"]
        return ["add_subject.html"]

    def get_initial(self):
        if self.subject:
            return {
                'name': self.subject.name,
                'description': self.subject.description
            }
        return super().get_initial()

    def form_valid(self, form):
        name = form.cleaned_data['name']
        description = form.cleaned_data['description']

        if self.subject:
            self.subject.name = name
            self.subject.description = description
        else:
            Subject.objects.create(
                name=name,
                description=description
            )

        return super().form_valid(form)


class SubjectDeleteFormView(LoginRequiredMixin, FormView):
    form_class = SubjectForm
    success_url = "/subjects_main/"

    def dispatch(self, request, *args, **kwargs):
        self.subject_id = kwargs.get('subject_id')
        self.subject = None
        if self.subject_id:
            self.subject = Subject.objects.get(id=self.subject_id)
        return super().dispatch(request, *args, **kwargs)

    def get_template_names(self):
        if self.subject:
            return ["edit_subject.html"]
        return ["add_subject.html"]

    def get_initial(self):
        if self.subject:
            return {
                'name': self.subject.name,
                'description': self.subject.description
            }
        return super().get_initial()

    def form_valid(self, form):
        self.subject.delete()

        return super().form_valid(form)
    
class ClassManageFormView(LoginRequiredMixin, FormView):
    form_class = ClassForm
    success_url = "/classes_main/"

    def dispatch(self, request, *args, **kwargs):
        self.class_id = kwargs.get('class_id')
        self.grade = None
        if self.class_id:
            self.grade = Class.objects.get(id=self.class_id)
        return super().dispatch(request, *args, **kwargs)

    def get_template_names(self):
        if self.grade:
            return ["edit_class.html"]
        return ["add_class.html"]

    def get_initial(self):
        if self.grade:
            return {
                'grade': self.grade.grade,
                'year': self.grade.year
            }
        return super().get_initial()

    def form_valid(self, form):
        grade = form.cleaned_data['grade']
        year = form.cleaned_data['year']

        if self.grade:
            self.grade.grade = grade
            self.grade.year = year
        else:
            Class.objects.create(
                grade=grade,
                year=year
            )

        return super().form_valid(form)


class ClassDeleteFormView(LoginRequiredMixin, FormView):
    form_class = ClassForm
    success_url = "/classes_main/"

    def dispatch(self, request, *args, **kwargs):
        self.class_id = kwargs.get('class_id')
        self.grade = None
        if self.class_id:
            self.grade = Class.objects.get(id=self.class_id)
        return super().dispatch(request, *args, **kwargs)

    def get_template_names(self):
        if self.grade:
            return ["edit_class.html"]
        return ["add_class.html"]

    def get_initial(self):
        if self.grade:
            return {
                'grade': self.grade.grade,
                'year': self.grade.year
            }
        return super().get_initial()

    def form_valid(self, form):
        self.grade.delete()

        return super().form_valid(form)


class StudentView(LoginRequiredMixin, View):

    def get_context_data(self, **kwargs):
        context = kwargs
        context["css_file"] = 'albums/styles.css'
        return context

    def get(self, request, student_id=None):
        if request.path == reverse('add_student'):
            context = self.get_context_data(grades=grades)
            context["students"] = Student.objects.select_related('grade').all()
            return render(request, 'add_student.html', context)
        if request.path == reverse('edit_list_student'):
            students = Student.objects.select_related('grade').all()
            context = self.get_context_data(students=students)
            return render(request, 'edit_list_student.html', context)
        if request.path == reverse('delete_list_student'):
            students = Student.objects.select_related('grade').all()
            context = self.get_context_data(students=students)
            return render(request, 'delete_list_student.html', context)
        if student_id:
            if request.path == reverse('edit_student', kwargs={'student_id': student_id}):
                return self.update(request, student_id)

            elif request.path == reverse('delete_student', kwargs={'student_id': student_id}):
                return self.delete(request, student_id)
        students = Student.objects.select_related('grade').all()
        context = self.get_context_data(students=students)
        return render(request, 'index.html', context)

    def post(self, request, student_id=None):
        if request.path == reverse('add_student'):
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            age = request.POST.get('age')
            grade = request.POST.get('grade')

            grade = Class.objects.get(grade=grade)
            student = Student(first_name=first_name, last_name=last_name, age=age, grade=grade)

            try:
                student.save()
                messages.success(request, 'Student created successfully!')
                return redirect('add_student')
            except IntegrityError as e:
                messages.error(request, f"Error: {str(e)}")

            return HttpResponseRedirect(reverse('add_student'))
        elif student_id:
            if request.path == reverse('edit_student', kwargs={'student_id': student_id}):
                return self.update(request, student_id)

            elif request.path == reverse('delete_student', kwargs={'student_id': student_id}):
                return self.delete(request, student_id)
        else:
            grades = Class.objects.all() 
            context = self.get_context_data(classes=grades)
            return render(request, 'add_student.html', context)

    def update(self, request, student_id):
        student = Student.objects.get(id=student_id)

        if request.method == 'POST':
            student.first_name = request.POST.get('first_name')
            student.last_name = request.POST.get('last_name')
            student.age = request.POST.get('age')
            grade = request.POST.get('grade')
            new_grade = Class.objects.get(grade=grade)
            student.grade = new_grade
            student.save()

            return HttpResponseRedirect(reverse('edit_list_student'))

        context = self.get_context_data(classes=grades, student=student)
        return render(request, 'edit_student.html', context)

    def delete(self, request, student_id):
        student = Student.objects.get(id=student_id)

        if request.method == 'POST':
            student.delete()
            return HttpResponseRedirect(reverse('delete_list_student'))

        context = self.get_context_data(classes=grades, student=student)
        return render(request, 'delete_student.html', context)


class TeacherView(LoginRequiredMixin, View):

    def get_context_data(self, **kwargs):
        context = kwargs
        context["css_file"] = 'albums/styles.css'
        return context

    def get(self, request, teacher_id=None):
        if request.path == reverse('add_teacher'):
            context = self.get_context_data(subjects=subjects)
            context["teachers"] = Teacher.objects.select_related('subject').all()
            return render(request, 'add_teacher.html', context)
        if request.path == reverse('edit_list_teacher'):
            teachers = Teacher.objects.select_related('subject').all()
            context = self.get_context_data(teachers=teachers)
            return render(request, 'edit_list_teacher.html', context)
        if request.path == reverse('delete_list_teacher'):
            teachers = Teacher.objects.select_related('subject').all()
            context = self.get_context_data(teachers=teachers)
            return render(request, 'delete_list_teacher.html', context)
        if teacher_id:
            if request.path == reverse('edit_teacher', kwargs={'teacher_id': teacher_id}):
                return self.update(request, teacher_id)

            elif request.path == reverse('delete_teacher', kwargs={'teacher_id': teacher_id}):
                return self.delete(request, teacher_id)
        teachers = Teacher.objects.select_related('subject').all()
        context = self.get_context_data(teachers=teachers)
        return render(request, 'teachers.html', context)

    def post(self, request, teacher_id=None):
        if request.path == reverse('add_teacher'):
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            subject = request.POST.get('subject')

            subject = Subject.objects.get(name=subject)

            teacher = Teacher(first_name=first_name, last_name=last_name, subject=subject)

            try:
                teacher.save() 
                messages.success(request, 'Teacher created successfully!')
            except IntegrityError as e:
                messages.error(request, f"Error: {str(e)}")
            
            return HttpResponseRedirect(reverse('add_teacher'))
        elif teacher_id:
            if request.path == reverse('edit_teacher', kwargs={'teacher_id': teacher_id}):
                return self.update(request, teacher_id)

            elif request.path == reverse('delete_teacher', kwargs={'teacher_id': teacher_id}):
                return self.delete(request, teacher_id)
        else:
            grades = Class.objects.all() 
            context = self.get_context_data(classes=grades)
            return render(request, 'add_student.html', context)

    def update(self, request, teacher_id):
        teacher = Teacher.objects.get(id=teacher_id)

        if request.method == 'POST':
            teacher = Teacher.objects.get(id=teacher_id)
            teacher.first_name = request.POST.get('first_name')
            teacher.last_name = request.POST.get('last_name')
            subject = request.POST.get('subject')
            new_subject = Subject.objects.get(name=subject)
            teacher.subject = new_subject
            teacher.save()
            
            return HttpResponseRedirect(reverse('edit_list_teacher'))

        context = self.get_context_data(subjects=subjects, teacher=teacher)
        return render(request, 'edit_teacher.html', context)

    def delete(self, request, teacher_id):
        teacher = Teacher.objects.get(id=teacher_id)

        if request.method == 'POST':
            teacher.delete()
            return HttpResponseRedirect(reverse('delete_list_teacher'))

        context = self.get_context_data(classes=grades, teacher=teacher)
        return render(request, 'delete_teacher.html', context)

class SubjectView(LoginRequiredMixin, View):

    def get_context_data(self, **kwargs):
        context = kwargs
        context["css_file"] = 'albums/styles.css'
        return context

    def get(self, request, subject_id=None):
        if request.path == reverse('add_subject'):
            return render(request, 'add_subject.html', context)
        if request.path == reverse('edit_list_subject'):
            context = self.get_context_data(subjects=subjects)
            return render(request, 'edit_list_subject.html', context)
        if request.path == reverse('delete_list_subject'):
            context = self.get_context_data(subjects=subjects)
            return render(request, 'delete_list_subject.html', context)
        if subject_id:
            if request.path == reverse('edit_subject', kwargs={'subject_id': subject_id}):
                return self.update(request, subject_id)

            elif request.path == reverse('delete_subject', kwargs={'subject_id': subject_id}):
                return self.delete(request, subject_id)
        subjects = Subject.objects.all()
        subject_dict = []
        for i in subjects:
            new_dict = {"sub": i, "teachers": i.teachers.all()}
            subject_dict.append(new_dict)
            print(i.teachers.all())
        context = self.get_context_data(subjects=subject_dict)
        return render(request, 'subjects.html', context)

    def post(self, request, subject_id=None):
        if request.path == reverse('add_subject'):
            name = request.POST.get('name')
            description = request.POST.get('description')
            subject = Subject(name=name, description=description)
            subject.save()
            
            return HttpResponseRedirect(reverse('add_subject'))
        elif subject_id:
            if request.path == reverse('edit_subject', kwargs={'subject_id': subject_id}):
                return self.update(request, subject_id)

            elif request.path == reverse('delete_subject', kwargs={'subject_id': subject_id}):
                return self.delete(request, subject_id)
        else:
            context = self.get_context_data()
            return render(request, 'add_subject.html', context)

    def update(self, request, subject_id):
        subject = Subject.objects.get(id=subject_id)

        if request.method == 'POST':
            subject = Subject.objects.get(id=subject_id)
            subject.name = request.POST.get('name')
            subject.description = request.POST.get('description')
            subject.save()
            
            return HttpResponseRedirect(reverse('edit_list_subject'))

        context = self.get_context_data(subject=subject)
        return render(request, 'edit_subject.html', context)

    def delete(self, request, subject_id):
        subject = Subject.objects.get(id=subject_id)

        if request.method == 'POST':
            subject.delete()
            return HttpResponseRedirect(reverse('delete_list_subject'))

        context = self.get_context_data(subject=subject)
        return render(request, 'delete_subject.html', context)

class ClassView(LoginRequiredMixin, View):

    def get_context_data(self, **kwargs):
        context = kwargs
        context["css_file"] = 'albums/styles.css'
        return context

    def get(self, request, class_id=None):
        if request.path == reverse('add_class'):
            return render(request, 'add_class.html', context)
        if request.path == reverse('edit_list_class'):
            context = self.get_context_data(classes=grades)
            return render(request, 'edit_list_class.html', context)
        if request.path == reverse('delete_list_class'):
            context = self.get_context_data(classes=grades)
            return render(request, 'delete_list_class.html', context)
        if class_id:
            if request.path == reverse('edit_class', kwargs={'class_id': class_id}):
                return self.update(request, class_id)

            elif request.path == reverse('delete_class', kwargs={'class_id': class_id}):
                return self.delete(request, class_id)
        classes = Class.objects.all()
        class_dict = []
        for i in classes:
            new_dict = {"class": i, "students": i.students.all()}
            class_dict.append(new_dict)
            print(i.students.all())
        context = self.get_context_data(classes=class_dict)
        return render(request, 'classes.html', context)

    def post(self, request, class_id=None):
        if request.path == reverse('add_class'):
            name = request.POST.get('class_name')
            year = request.POST.get('year')

            grade = Class(grade=name, year=year)
            print(grade)

            try:
                grade.save() 
                messages.success(request, 'Grade created successfully!')
            except IntegrityError as e:
                messages.error(request, f"Error: {str(e)}")
            
            return HttpResponseRedirect(reverse('add_class'))
        elif class_id:
            if request.path == reverse('edit_class', kwargs={'class_id': class_id}):
                return self.update(request, class_id)

            elif request.path == reverse('delete_class', kwargs={'class_id': class_id}):
                return self.delete(request, class_id)
        else:
            context = self.get_context_data()
            return render(request, 'add_class.html', context)

    def update(self, request, class_id):
        grade = Class.objects.get(id=class_id)

        if request.method == 'POST':
            grade = Class.objects.get(id=class_id)
            grade.grade = request.POST.get('grade')
            grade.year = request.POST.get('year')
            grade.save()
            
            return HttpResponseRedirect(reverse('edit_list_class'))

        context = self.get_context_data(grade=grade)
        return render(request, 'edit_class.html', context)

    def delete(self, request, class_id):
        grade = Class.objects.get(id=class_id)

        if request.method == 'POST':
            grade.delete()
            return HttpResponseRedirect(reverse('delete_list_class'))

        context = self.get_context_data(grade=grade)
        return render(request, 'delete_class.html', context)
        

class MainPagesView(LoginRequiredMixin, View):

    def get_context_data(self, **kwargs):
        context = kwargs
        context["css_file"] = 'albums/styles.css'
        return context

    def get(self, request):
        if request.path == reverse('students_main'):
            context = self.get_context_data()
            return render(request, 'students_main.html', context)
        if request.path == reverse('teachers_main'):
            context = self.get_context_data()
            return render(request, 'teachers_main.html', context)
        if request.path == reverse('subjects_main'):
            context = self.get_context_data()
            return render(request, 'subjects_main.html', context)
        if request.path == reverse('classes_main'):
            context = self.get_context_data()
            return render(request, 'classes_main.html', context)

class HomeShow(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["css_file"] = 'albums/styles.css'
        return context

class TxtDownload(View):
    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='text/plain')
        if request.path == reverse('get_txt_students'):
            response['Content-Disposition'] = 'attachment; filename="students_info.txt"'

            students = Student.objects.select_related('grade').all()

            response.write("Students List\n")
            num = 1
            for student in students:
                student_info = f"{num}. Name and Surname: {student.first_name} {student.last_name}\n Age: {student.age}\n Class: {student.grade}\n"
                response.write(student_info)
                num += 1

            return response
        if request.path == reverse('get_txt_teachers'):
            response['Content-Disposition'] = 'attachment; filename="teachers_info.txt"'

            teachers = Teacher.objects.select_related('subject').all()

            response.write("Teachers List\n")
            num = 1
            for teacher in teachers:
                teacher_info = f"{num}. Name and Surname: {teacher.first_name} {teacher.last_name}\n Subject: {teacher.subject}\n"
                response.write(teacher_info)
                num += 1

            return response
        if request.path == reverse('get_txt_subjects'):
            response['Content-Disposition'] = 'attachment; filename="subjects_info.txt"'

            subjects = Subject.objects.all()

            response.write("Subjects List\n")
            num = 1
            
            for subject in subjects:
                print(subject)
                subject_info = f"{num}. Name: {subject.name}\n Description: {subject.description}\n"
                info = ''
                for i in subject.teachers.all():
                    info += f"Teacher: {i.first_name} {i.last_name}\n"
                subject_info += info
                response.write(subject_info)
                num += 1

            return response
        if request.path == reverse('get_txt_classes'):
            response['Content-Disposition'] = 'attachment; filename="classes_info.txt"'

            classes = Class.objects.all()

            response.write("Classes List\n")
            num = 1
            for grade in classes:
                print(grade)
                class_info = f"{num}. Name: {grade.grade}\n Year: {grade.year}\n"
                info = ''
                for i in grade.students.all():
                    info += f"Student: {i.first_name} {i.last_name}\n"
                class_info += info
                response.write(class_info)
                num += 1

            return response

class ExcelDownload(View):
    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        if request.path == reverse('get_excel_students'):
            response['Content-Disposition'] = 'attachment; filename=NewExcel.xlsx'

            students = Student.objects.select_related('grade').all()
            students_list = []
            for i in students:
                new_list = ["First Name", i.first_name]
                new_list1 = ["Last Name", i.last_name]
                new_list2 = ["Age", str(i.age)]
                
                students_list.append(new_list)
                students_list.append(new_list1)
                students_list.append(new_list2)
                if i.grade != None:
                    new_list3 = ["Grade", i.grade.grade]
                    students_list.append(new_list3)

        if request.path == reverse('get_excel_teachers'):
            response['Content-Disposition'] = 'attachment; filename=NewExcel.xlsx'

            teachers = Teacher.objects.select_related('subject').all()
            teachers_list = []
            for i in teachers:
                new_list = ["First Name", i.first_name]
                new_list1 = ["Last Name", i.last_name]
                
                teachers_list.append(new_list)
                teachers_list.append(new_list1)
                if i.subject != None:
                    new_list2 = ["Subject", i.subject.name]
                    teachers_list.append(new_list2)
        if request.path == reverse('get_excel_subjects'):
            response['Content-Disposition'] = 'attachment; filename=NewExcel.xlsx'

            subjects = Subject.objects.all()
            sub_list = []
            for i in subjects:
                new_list = ["Name", i.name]
                new_list1 = ["Description", i.description]
                info = ''
                for n in i.teachers.all():
                    info += f"{n.first_name} {n.last_name}\n"
                new_list2 = ["Teachers", info]
                sub_list.append(new_list)
                sub_list.append(new_list1)
                sub_list.append(new_list2)
            
            
        if request.path == reverse('get_excel_classes'):
            response['Content-Disposition'] = 'attachment; filename=NewExcel.xlsx'

            classes = Class.objects.all()
            class_list = []
            for i in classes:
                new_list = ["Name", i.grade]
                new_list1 = ["Year", i.year]
                info = ''
                for n in i.students.all():
                    info += f"{n.first_name} {n.last_name}\n"
                new_list2 = ["Students", info]
                class_list.append(new_list)
                class_list.append(new_list1)
                class_list.append(new_list2)
            
        workbook = xlsxwriter.Workbook('NewExcel.xlsx')
        worksheet = workbook.add_worksheet()

        row = 0
        col = 0

        for i in class_list:
            header = i[0]
            value = i[1]
            worksheet.write(row, col, header)
            worksheet.write(row, col + 1, value)
            row += 1
            
        workbook.close()

        with open('NewExcel.xlsx', 'rb') as f:
            response.write(f.read())

        return response


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                login(self.request, user)
                return super().form_valid(form)
            else:
                form.add_error(None, 'Password or email incorrect')
        except user is None:
            form.add_error(None, 'User not found')
        return self.form_invalid(form)
        #user = authenticate(self.request, username=username, password=password)
        #if user is not None:
            #login(self.request, user)
            #return super().form_valid(form)
        #else:
            #form.add_error(None, 'Невірний логін або пароль')
            #return self.form_invalid(form)

class CheckShow(TemplateView):
    template_name = 'check_email.html'
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["css_file"] = 'albums/styles.css'
        return context

#class ForgotPassView(FormView):
    #template_name = 'forgot_pass.html'
    #form_class = ForgotForm
    #success_url = reverse_lazy('check_email')

    #def form_valid(self, form):
        #email = form.cleaned_data['email']
        #new_password1 = []
        #for i in range(8):
            #new_password = random.choice(string.digits)
            #new_password1.append(new_password)
        #message = ''.join(new_password1)
        #root = '\nFollow this root -> http://127.0.0.1:8000/change_pass'
        #message += root
        #you = email
        #msg = MIMEText(message)
        #msg['Subject'] = 'New password'
        #msg['From'] = me
        #msg['To'] = you

        #with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            #server.login(me, password)
            #server.sendmail(me, [you], msg.as_string())
        
        #self.request.session['email_for_pass_change'] = email
        #return super().form_valid(form)

    #def form_invalid(self, form):
        #return super().form_invalid(form)

class ChangePassView(FormView):
    template_name = 'change_pass.html'
    form_class = ChangeForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        email = self.request.session.get('email_for_pass_change')
        pasw = form.cleaned_data['pasw']
        try:
            user = User.objects.get(email=email)
            user.set_password(pasw)
            user.save()
            return super().form_valid(form)
        except User.DoesNotExist:
            form.add_error(None, 'User not found')
    
        return super().form_invalid(form)
        

class RegisterView(FormView):
    template_name = 'register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')


