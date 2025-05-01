from django import forms
from .models import Student, Class, Teacher, Subject
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password


class StudentForm(forms.Form):
    first_name = forms.CharField(
        label="First Name",
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'George',
            'autofocus': 'autofocus',
        }),
        help_text="Write first name."
    )

    last_name = forms.CharField(
        label="Last Name",
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Welly'
        }),
        help_text="Write last name."
    )

    age = forms.IntegerField(
        label="Age",
        required=True,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'For example: 13, 15, 11'
        }),
        help_text="Write your age."
    )

    grade = forms.ModelChoiceField(
        queryset=Class.objects.all(),
        label="Class",
        empty_label="Choose class",
        widget=forms.Select(attrs={
            'class': 'form-select'
        }),
        help_text="Choose class from the list."
    )

class StudentDeleteForm(forms.Form):
    first_name = forms.CharField(
        label="First Name",
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'readonly': 'readonly'
        })
    )

    last_name = forms.CharField(
        label="Last Name",
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'readonly': 'readonly'
        })
    )

    age = forms.IntegerField(
        label="Age",
        required=True,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'readonly': 'readonly'
        })
    )

    grade = forms.ModelChoiceField(
        queryset=Class.objects.all(),
        label="Class",
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-select',
            'disabled': 'disabled'
        })
    )




class TeacherForm(forms.Form):
    first_name = forms.CharField(
        label="First Name",
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Lukas',
            'autofocus': 'autofocus',
        }),
        help_text="Write first name."
    )

    last_name = forms.CharField(
        label="Last Name",
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Amobi'
        }),
        help_text="Write last name."
    )

    subject = forms.ModelChoiceField(
        queryset=Subject.objects.all(),
        label="Subject",
        empty_label="Choose subject",
        widget=forms.Select(attrs={
            'class': 'form-select'
        }),
        help_text="Choose subject from the list."
    )

class TeacherDeleteForm(forms.Form):
    first_name = forms.CharField(
        label="First Name",
        max_length=50,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'readonly': 'readonly'
        })
    )

    last_name = forms.CharField(
        label="Last Name",
        max_length=50,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'readonly': 'readonly'
        })
    )

    subject = forms.ModelChoiceField(
        queryset=Subject.objects.all(),
        label="Subject",
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-select',
            'disabled': 'disabled'
        })
    )


class SubjectForm(forms.Form):
    name = forms.CharField(
        label="Name",
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Math',
            'autofocus': 'autofocus',
        }),
        help_text="Write name of the subject."
    )

    description = forms.CharField(
        label="Description",
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Here we learn math.'
        }),
        help_text="Write description of the subject."
    )

class SubjectDeleteForm(forms.Form):
    name = forms.CharField(
        label="Name",
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'readonly': 'readonly'
        })
    )

    description = forms.CharField(
        label="Description",
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'readonly': 'readonly'
        })
    )


class ClassForm(forms.Form):
    grade = forms.CharField(
        label="Grade",
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '3-A',
            'autofocus': 'autofocus',
        }),
        help_text="Write name of the class."
    )

    year = forms.IntegerField(
        label="Year",
        required=True,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': '1979'
        }),
        help_text="Write year of the class."
    )

class ClassDeleteForm(forms.Form):
    grade = forms.CharField(
        label="Grade",
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'readonly': 'readonly'
        }),
        help_text="Write name of the class."
    )

    year = forms.IntegerField(
        label="Year",
        required=True,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'readonly': 'readonly'
        }),
        help_text="Write year of the class."
    )

class LoginForm(forms.Form):
    #username = forms.CharField(max_length=100)
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

class ForgotForm(forms.Form):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))

class ChangeForm(forms.Form):
    pasw = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

class CustomUserCreationForm(forms.Form):
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
        help_text="Password must be at least 8 characters and contain numbers, symbols and letters.")
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
        help_text="Please, confirm your password.")
    
    def clean_password1(self):
        password1 = self.cleaned_data.get("password")
        validate_password(password1)

        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("confirm_password")
        
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password']
        )
        return user 


