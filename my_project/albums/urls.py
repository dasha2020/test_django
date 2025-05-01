from django.urls import path
from . import views
from .views import *
from .services.email_service import ForgotPassView

urlpatterns = [
    #path('students/', views.show_students, name='show_students'),
    #path('home/', views.home, name='home'),
    #path('get_txt_students/', views.get_txt_students, name='get_txt_students'),
    #path('get_txt_teachers/', views.get_txt_teachers, name='get_txt_teachers'),
    #path('get_txt_subjects/', views.get_txt_subjects, name='get_txt_subjects'),
    #path('get_txt_classes/', views.get_txt_classes, name='get_txt_classes'),
    #path('teachers/', views.show_teachers, name='show_teachers'),
    #path('subjects/', views.show_subjects, name='show_subjects'),
    #path('class/', views.show_classes, name='show_classes'),
    #path('get_excel_classes/', views.get_excel_classes, name='get_excel_classes'),
    #path('get_excel_subjects/', views.get_excel_subjects, name='get_excel_subjects'),
    #path('get_excel_teachers/', views.get_excel_teachers, name='get_excel_teachers'),
    #path('get_excel_students/', views.get_excel_students, name='get_excel_students'),
    #path('add_student/', views.add_student, name='add_student'),
    #path('add_teacher/', views.add_teacher, name='add_teacher'),
    #path('add_subject/', views.add_subject, name='add_subject'),
    #path('add_class/', views.add_class, name='add_class'),

    #path('edit_student/<int:student_id>/', views.edit_student, name='edit_student'),
    #path('edit_teacher/<int:teacher_id>/', views.edit_teacher, name='edit_teacher'),
    #path('edit_subject/<int:subject_id>/', views.edit_subject, name='edit_subject'),
    #path('edit_class/<int:class_id>/', views.edit_class, name='edit_class'),

    #path('delete_student/<int:student_id>/', views.delete_student, name='delete_student'),
    #path('delete_teacher/<int:teacher_id>/', views.delete_teacher, name='delete_teacher'),
    #path('delete_subject/<int:subject_id>/', views.delete_subject, name='delete_subject'),
    #path('delete_class/<int:class_id>/', views.delete_class, name='delete_class'),

    #path('edit_list_student/', views.edit_list_student, name='edit_list_student'),
    #path('edit_list_teacher/', views.edit_list_teacher, name='edit_list_teacher'),
    #path('edit_list_subject/', views.edit_list_subject, name='edit_list_subject'),
    #path('edit_list_class/', views.edit_list_class, name='edit_list_class'),

    #path('delete_list_student/', views.delete_list_student, name='delete_list_student'),
    #path('delete_list_teacher/', views.delete_list_teacher, name='delete_list_teacher'),
    #path('delete_list_subject/', views.delete_list_subject, name='delete_list_subject'),
    #path('delete_list_class/', views.delete_list_class, name='delete_list_class'),

    #classes

    path('students/', StudentView.as_view(), name='show_students'), #new class
    path('teachers/', TeacherView.as_view(), name='show_teachers'),
    path('subjects/', SubjectView.as_view(), name='show_subjects'),
    path('class/', ClassView.as_view(), name='show_classes'),
    path('home/', HomeShow.as_view(), name='home'),
    path('get_txt_students/', TxtDownload.as_view(), name='get_txt_students'),
    path('get_txt_teachers/', TxtDownload.as_view(), name='get_txt_teachers'),
    path('get_txt_subjects/', TxtDownload.as_view(), name='get_txt_subjects'),
    path('get_txt_classes/', TxtDownload.as_view(), name='get_txt_classes'),
    path('get_excel_classes/', ExcelDownload.as_view(), name='get_excel_classes'),
    path('get_excel_subjects/', ExcelDownload.as_view(), name='get_excel_subjects'),
    path('get_excel_teachers/', ExcelDownload.as_view(), name='get_excel_teachers'),
    path('get_excel_students/', ExcelDownload.as_view(), name='get_excel_students'),

    path('add_student/', StudentManageFormView.as_view(), name='add_student'), #new class
    path('add_teacher/', TeacherManageFormView.as_view(), name='add_teacher'),
    path('add_subject/', SubjectManageFormView.as_view(), name='add_subject'),
    path('add_class/', ClassManageFormView.as_view(), name='add_class'),

    path('edit_student/<int:student_id>/', StudentManageFormView.as_view(), name='edit_student'), #new class
    path('edit_teacher/<int:teacher_id>/', TeacherManageFormView.as_view(), name='edit_teacher'),
    path('edit_subject/<int:subject_id>/', SubjectManageFormView.as_view(), name='edit_subject'),
    path('edit_class/<int:class_id>/', ClassManageFormView.as_view(), name='edit_class'),

    path('delete_student/<int:student_id>/', StudentDeleteFormView.as_view(), name='delete_student'), #new class
    path('delete_teacher/<int:teacher_id>/', TeacherDeleteFormView.as_view(), name='delete_teacher'),
    path('delete_subject/<int:subject_id>/', SubjectDeleteFormView.as_view(), name='delete_subject'),
    path('delete_class/<int:class_id>/', ClassDeleteFormView.as_view(), name='delete_class'),

    path('edit_list_student/', StudentView.as_view(), name='edit_list_student'),
    path('edit_list_teacher/', TeacherView.as_view(), name='edit_list_teacher'),
    path('edit_list_subject/', SubjectView.as_view(), name='edit_list_subject'),
    path('edit_list_class/', ClassView.as_view(), name='edit_list_class'),

    path('delete_list_student/', StudentView.as_view(), name='delete_list_student'),
    path('delete_list_teacher/', TeacherView.as_view(), name='delete_list_teacher'),
    path('delete_list_subject/', SubjectView.as_view(), name='delete_list_subject'),
    path('delete_list_class/', ClassView.as_view(), name='delete_list_class'),

    path('students_main/', MainPagesView.as_view(), name='students_main'), #new class
    path('teachers_main/', MainPagesView.as_view(), name='teachers_main'),
    path('subjects_main/', MainPagesView.as_view(), name='subjects_main'),
    path('class_main/', MainPagesView.as_view(), name='classes_main'),


    path('accounts/login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('new_password/', ForgotPassView.as_view(), name='forgot'),
    path('check_email/', CheckShow.as_view(), name='check_email'),
    path('change_pass/', ChangePassView.as_view(), name='change_pass'),
]
