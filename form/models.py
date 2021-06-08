from django.db import models

# Create your models here.
from django.db import models
from django.db.models.deletion import CASCADE
from datetime import datetime, date
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.
GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Others', 'Others'),
)

APPLY_CHOICES = (
    ('Student', 'Student'),
    ('Disability', 'Disability'),
    ('Widow', 'Widow'),
    ('Marriage', 'Marriage'),
    ('BPL', 'BPL'),
    ('Caste', 'Caste'),
    ('Senior Citizen', 'Senior Citizen'),
)

MARITAL_STATUS = (
    ('Unmarried', 'Unmarried'),
    ('Married', 'Married'),
    ('Widow', 'Widow'),
)

CASTE_CHOICES = (
    ('General', 'General'),
    ('OBC', 'OBC'),
    ('SC', 'SC'),
    ('ST', 'ST'),
)
COMMUNITY_CHOICES = (
    ('Hindu', 'Hindu'),
    ('Muslim', 'Muslim'),
    ('Christianity', 'Christianity'),
    ('Others', 'Others'),
)
EDUCATION_CHOICES = (
    ('Day scholar', 'Day scholar'),
    ('Hosteller', 'Hosteller'),
    ('Correspondence', 'Correspondence'),
)
BOOLEAN_CHOICES = (
    ('Yes', 'Yes'),
    ('No', 'No'),

)
DISABILITY_CHOICES = (
    ('Yes', 'Yes'),
    ('No', 'No'),

)



class Personal_detail(models.Model):
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    Fullname = models.CharField(max_length=255)
    Email_Address = models.EmailField()
    Gender = models.CharField(max_length=50, choices=GENDER_CHOICES)
    Age = models.PositiveIntegerField(null=True, blank=False)
    Date_of_birth = models.DateField(auto_now_add=False, auto_now=False, blank=False, help_text='Please Enter the following in YYYY-MM-DD')
    Aadhar_number = models.CharField(max_length=12, unique=True)
    Marital_status = models.CharField(max_length=50, choices=MARITAL_STATUS)
    Father_name = models.CharField(max_length=255)
    Father_occupation = models.CharField(max_length=255)
    Father_number = models.CharField(max_length=10, blank=True, null=True, help_text= 'If minor, Please mention')
    Mother_name = models.CharField(max_length=255)
    Mother_occupation = models.CharField(max_length=255)
    Guardian_name = models.CharField(max_length=255, null=True, blank=True)
    Guardian_occupation = models.CharField(max_length=255, null=True, blank=True)
    Mobile_number = models.CharField(max_length=10)
    Address_1 = models.CharField(max_length=900,)
    Address_2 = models.CharField(max_length=900, blank=True, null=True)
    City = models.CharField(max_length=100)
    District = models.CharField(max_length=100)
    Zipcode = models.CharField(max_length=8)
    Annual_income = models.PositiveIntegerField(null=True, blank=False)
    Caste = models.CharField(max_length=50, choices=CASTE_CHOICES)
    Community = models.CharField(max_length=50, choices=COMMUNITY_CHOICES)
    course_pursuing = models.CharField(max_length=255, help_text='eg: B.sc,B.tech,...')
    specialization = models.CharField(max_length=255, help_text='eg: ECE,Pharmacy,Nursing,...')
    roll_number = models.CharField(max_length=8, help_text='eg: university roll number')
    mark_in_higher_school = models.CharField(max_length=5, help_text='Enter it in marks or average eg: 6.9,8.8')
    mark_in_secondary_school = models.CharField(max_length=5, help_text='Enter it in points eg: 6.9,8.8')
    Education_mode = models.CharField(max_length=50, choices=EDUCATION_CHOICES)
    scholarship = models.CharField(max_length=50, choices=BOOLEAN_CHOICES, help_text='Availing any scholarship already? If yes, Please mention below')
    mention_scholarship = models.CharField(max_length=500, help_text='if not leave blank', blank=True, null=True)
    disability = models.CharField(max_length=50, choices=DISABILITY_CHOICES, help_text='do you have any disabilities? If yes, Please mention below')
    mention = models.CharField(max_length=500, help_text='if disability please mention', blank=True, null=True)
    applying_for = models.CharField(help_text='You"re applying for',max_length=50, choices=APPLY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "User - {} UUID- {} ".format(self.Fullname, self.Aadhar_number)
    
    def get_absolute_url(self):
        return reverse('form_detail', args=[str(self.id)])