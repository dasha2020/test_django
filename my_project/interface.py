import django
import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_project.settings')
django.setup()

from albums.models import Subject, Teacher, Class, Student

def create_subject():
    name = input("Input name of the subject:  ")
    description = input("Input description of the subject (if needed):  ")
    
    subject = Subject(name=name, description=description)
    subject.save()
    print(subject.name, " added")

def create_teacher():
    name = input("Input name:   ")
    surname = input("Input surname:   ")
    subject = input("Input subject:   ")
    s = Subject.objects.get(name=subject)
    if s:
        teacher = Teacher(first_name=name, last_name=surname, subject=s)
        teacher.save()
    else:
        descr = f"We learn {subject} here"
        s_new = Subject(name=subject, description=descr)
        teacher = Teacher(first_name=name, last_name=surname, subject=s_new)
        teacher.save()
    
    print(f"{teacher.first_name} {teacher.last_name}", "added")

def create_class():
    name = input("Input name of the class:  ")
    year = input("Input year of the class (if needed):  ")
    
    grade = Class(name=name, year=year)
    grade.save()
    print(grade.grade, " added")

def create_student():
    name = input("Input name:   ")
    surname = input("Input surname:   ")
    grade = input("Input grade:   ")
    year = input("Input year of the class (if needed):  ")
    s = Class.objects.get(name=grade)
    if s:
        student = Student(first_name=name, last_name=surname, grade=s)
        student.save()
    else:
        s_new = Class(grade=grade, year=year)
        student = Student(first_name=name, last_name=surname, grade=s_new)
        student.save()

def delete_subject(subject_name):
    subject = Subject.objects.get(name=subject_name)
    subject.delete()
    print(subject_name, " delete")

def delete_teacher(teacher_lastname):
    teacher = Teacher.objects.get(name=teacher_lastname)
    teacher.delete()
    print(teacher_lastname, " delete")

def delete_class(class_name):
    grade = Class.objects.get(name=class_name)
    grade.delete()
    print(class_name, " delete")

def delete_student(student_lastname):
    student = Student.objects.get(name=student_lastname)
    student.delete()
    print(student_lastname, " delete")

def edit_subject(subject):
    find_subject = Subject.objects.get(name=subject)
    name_or_descr = input("Name (1) or description (2)?   ")
    if name_or_descr == "1":
        name = input("Input new name of the subject:  ")
        q = input("Do you want to change description [y/n]?   ")
        if q == "y":
            description = input("Input new description of the subject (if needed):  ")
            find_subject.name = name
            find_subject.description = description
            print("Subject name and description changed")
        else:
            find_subject.name = name
            print("Subject name changed")
    elif name_or_descr == "2":
        description = input("Input new description of the subject (if needed):  ")
        q = input("Do you want to change name [y/n]?   ")
        if q == "y":
            name = input("Input new name of the subject:  ")
            find_subject.name = name
            find_subject.description = description
            print("Subject name and description changed")
        else:
            find_subject.description = description
            print("Subject description changed")

    
    find_subject.save()

def edit_teacher(teacher):
    find_teacher = Teacher.objects.get(last_name=teacher)
    change = input("Name (1) or last name (2) or subject(3)?   ")
    if change == "1":
        name = input("Input new name of the teacher:  ")
        q = input("Do you want to change last name [y/n]?   ")
        if q == "y":
            last_name = input("Input new last name of the teacher:  ")
            find_teacher.last_name = last_name
            find_teacher.first_name = name
        else:
            find_teacher.first_name = name
        q = input("Do you want to change subject [y/n]?   ")
        if q == "y":
            subject = input("Input new subject of the teacher:  ")
            s = Subject.objects.get(name=subject)
            if s:
                find_teacher.subject = s
                print("Teacher changes made")
            else:
                descr = f"We learn {subject} here"
                s_new = Subject(name=subject, description=descr)
                find_teacher.subject = s_new
                print("Teacher changes made")

    elif change == "2":
        last_name = input("Input new last_name of the teacher:  ")
        q = input("Do you want to change name [y/n]?   ")
        if q == "y":
            name = input("Input new name of the teacher:  ")
            find_teacher.first_name = name
            find_teacher.last_name = last_name
            print("Teacher changes made")
        else:
            find_teacher.last_name = last_name
            
        q = input("Do you want to change subject [y/n]?   ")
        if q == "y":
            subject = input("Input new subject of the teacher:  ")
            s = Subject.objects.get(name=subject)
            if s:
                find_teacher.subject = s
                print("Teacher changes made")
            else:
                descr = f"We learn {subject} here"
                s_new = Subject(name=subject, description=descr)
                find_teacher.subject = s_new
                print("Teacher changes made")
        else:
            print("Teacher changes made")
    
    elif change == "3":
        subject = input("Input new subject of the teacher:  ")
        s = Subject.objects.get(name=subject)
        if s:
            find_teacher.subject = s
            print("Teacher changes made")
        else:
            descr = f"We learn {subject} here"
            s_new = Subject(name=subject, description=descr)
            find_teacher.subject = s_new
            print("Teacher changes made")
        q = input("Do you want to change name [y/n]?   ")
        if q == "y":
            name = input("Input new name of the teacher:  ")
            find_teacher.first_name = name
            print("Teacher changes made")
            
        q = input("Do you want to change last name [y/n]?   ")
        if q == "y":
            last_name = input("Input new last name of the teacher:  ")
            find_teacher.last_name = last_name
    
    find_teacher.save()

def edit_class(grade):
    find_class = Class.objects.get(name=grade)
    change = input("Grade (1) or year (2)?   ")
    if change == "1":
        name = input("Input new name of the grade:  ")
        q = input("Do you want to change year [y/n]?   ")
        if q == "y":
            year = input("Input new year of sthe grade:  ")
            find_class.year = year
            find_class.grade = name
            print("Grade name and year changed")
        else:
            find_class.grade = name
            print("Grade name changed")
    elif change == "2":
        year = input("Input new year of the grade:  ")
        q = input("Do you want to change name [y/n]?   ")
        if q == "y":
            name = input("Input new name of the grade:  ")
            find_class.grade = name
            find_class.year = year
            print("Grade name and description changed")
        else:
            find_class.year = year
            print("Grade year changed")

    
    find_class.save()


def edit_student(student):
    find_student = Student.objects.get(last_name=student)
    q = input("Do you want to change first name [y/n]?   ")
    if q == "y":
        name = input("Input new name of the student:  ")
        find_student.first_name = name
    q = input("Do you want to change last name [y/n]?   ")
    if q == "y":
        last_name = input("Input new last name of the student:  ")
        find_student.last_name = last_name
    q = input("Do you want to change grade [y/n]?   ")
    if q == "y":
        grade = input("Input new grade of the student:  ")
        s = Class.objects.get(name=grade)
        if s:
            find_student.grade = s
        else:
            year = int(input("Input year of the grade:  "))
            s_new = Class(name=grade, year=year)
            find_student.grade = s_new
    q = input("Do you want to change age [y/n]?   ")
    if q == "y":
        age = int(input("Input new age of the student:  "))
        find_student.age = age
    
    find_student.save()
    print("Student changes made")


mes = input("1 - add subject; 2 - add teacher; 3 - add class; 4 - add student; 5 - edit; 6 - delete; 7- quit   ")
while mes != "7":
    if mes == "1":
        create_subject()
    elif mes == "2":
        create_teacher()
    elif mes == "3":
        create_class()
    elif mes == "4":
        create_student()
    elif mes == "5":
        edit_mes = input("1 - edit subject; 2 - edit teacher; 3 - edit student; 4 - edit class   ")
        if edit_mes == "1": 
            all_subjects = Subject.objects.all()
            for i in range(len(all_subjects)):
                print(f"{i+1}. {all_subjects[i]}")
            choose_subject = input("Choose subject to edit (input subject's name)   ")
            edit_subject(choose_subject)
        elif edit_mes == "2": 
            all_teachers = Teacher.objects.all()
            for i in range(len(all_teachers)):
                print(f"{i+1}. {all_teachers[i]}")
            choose_teacher = input("Choose teacher to edit (input teacher's last name)   ")
            edit_teacher(choose_teacher)
        elif edit_mes == "3": 
            all_students = Student.objects.all()
            for i in range(len(all_students)):
                print(f"{i+1}. {all_students[i]}")
            choose_student = input("Choose student to edit (input student's last name)   ")
            edit_student(choose_student)
        elif edit_mes == "4": 
            all_class = Class.objects.all()
            for i in range(len(all_class)):
                print(f"{i+1}. {all_class[i]}")
            choose_class = input("Choose class to edit (input class's name)   ")
            edit_class(choose_class)
    elif mes == "6":
        edit_mes = input("1 - delete subject; 2 - delete teacher; 3 - delete student; 4 - delete class")
        if edit_mes == "1": 
            all_subjects = Subject.objects.all()
            for i in range(len(all_subjects)):
                print(f"{i+1}. {all_subjects[i]}")
            choose_subject = input("Choose subject to delete (input subject's name)   ")
            delete_subject(choose_subject)
        elif edit_mes == "2": 
            all_teachers = Teacher.objects.all()
            for i in range(len(all_teachers)):
                print(f"{i+1}. {all_teachers[i]}")
            choose_teacher = input("Choose teacher to edit (input teacher's last name)   ")
            delete_teacher(choose_teacher)
        elif edit_mes == "3": 
            all_students = Student.objects.all()
            for i in range(len(all_students)):
                print(f"{i+1}. {all_students[i]}")
            choose_student = input("Choose student to edit (input student's last name)   ")
            delete_student(choose_student)
        elif edit_mes == "4": 
            all_class = Class.objects.all()
            for i in range(len(all_class)):
                print(f"{i+1}. {all_class[i]}")
            choose_class = input("Choose class to edit (input class's name)   ")
            delete_class(choose_class)
    mes = input("1 - add subject; 2 - add teacher; 3 - add class; 4 - add student; 5 - edit; 6 - delete; 7 - quit   ")


    