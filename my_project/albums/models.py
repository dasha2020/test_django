from django.db import models

# Create your models here.

class Album(models.Model): 
	title = models.CharField(max_length = 30) 
	artist = models.CharField(max_length = 30) 
	genre = models.CharField(max_length = 30) 

	def __str__(self): 
		return self.title 

class Song(models.Model): 
	name = models.CharField(max_length = 100) 
	album = models.ForeignKey(Album, on_delete = models.CASCADE) 

	def __str__(self): 
		return self.name 

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    roles = [
        ('admin', 'Admin'),
        ('user', 'User'),
    ]
    role = models.CharField(max_length=5, choices=roles, default='user')

    def __str__(self):
        return f"{self.name} - {self.role}"

class Task(models.Model):
    statuses = [
        ('in_progress', 'In progress'),
        ('completed', 'Completed'),
        ('postponed', 'Postponed'),
    ]
    
    title = models.CharField(max_length=100)  
    description = models.TextField()
    status = models.CharField(max_length=15, choices=statuses, default='in_progress')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.user}"

class Post(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.date}"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.text}"



class Subject(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(null=True)

    class Meta:
        constraints = [

            models.CheckConstraint(check=models.Q(name__regex='^[\D]*$'), name='name_has_no_digits'),

            models.UniqueConstraint(fields=['name'], name='unique_name'),
        ]

    def __str__(self):
        return f"{self.name}"

class Teacher(models.Model):
    first_name = models.CharField(max_length=30)  
    last_name = models.CharField(max_length=30)  
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, related_name='teachers', null=True)

    class Meta:
        constraints = [

            models.CheckConstraint(check=models.Q(first_name__regex='^[A-Z]'), name='first_name_starts_uppercase'),
            models.CheckConstraint(check=models.Q(last_name__regex='^[A-Z]'), name='last_name_starts_uppercase'),
            models.CheckConstraint(check=models.Q(first_name__regex='^[\D]*$'), name='first_name_has_no_digits'),
            models.CheckConstraint(check=models.Q(last_name__regex='^[\D]*$'), name='last_name_has_no_digits'),

            models.UniqueConstraint(fields=['first_name', 'last_name'], name='unique_first_name'),
        ]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Class(models.Model):
    grade = models.CharField(max_length=10)
    year = models.IntegerField(null=True)

    class Meta:
        constraints = [

            models.CheckConstraint(check=models.Q(year__regex='^\d+$'), name='year_has_only_digits'),

            models.UniqueConstraint(fields=['grade'], name='unique_grade'),
        ]

    def __str__(self):
        return f"{self.grade}"

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(null=True)
    grade = models.ForeignKey(Class, on_delete=models.SET_NULL, related_name='students', null=True)

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(age__gte=0) & models.Q(age__lte=18), name='age_between_zero_and_eighteen'),

            models.CheckConstraint(check=models.Q(first_name__regex='^[A-Z]'), name='first_name_student_starts_uppercase'),
            models.CheckConstraint(check=models.Q(last_name__regex='^[A-Z]'), name='last_name_student_starts_uppercase'),
            models.CheckConstraint(check=models.Q(first_name__regex='^[\D]*$'), name='first_name_student_has_no_digits'),
            models.CheckConstraint(check=models.Q(last_name__regex='^[\D]*$'), name='last_name_student_has_no_digits'),

            models.UniqueConstraint(fields=['first_name', 'last_name'], name='unique_first_name_student'),
        ]

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.grade}"
