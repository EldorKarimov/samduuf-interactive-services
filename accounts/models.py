from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password


class Student(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    third_name = models.CharField(max_length=50, blank=True)
    full_name = models.CharField(max_length=128, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=13, null=True, blank=True)
    student_id_number = models.PositiveBigIntegerField(null=True, blank=True)
    university = models.CharField(max_length=128, blank=True)
    faculty = models.CharField(max_length=128, blank=True)
    group = models.CharField(max_length=50, blank=True)
    specialty = models.CharField(max_length=128, blank=True)
    occommodation = models.CharField(max_length=50, blank=True)
    district = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=255, blank=True)
    eduForm = models.CharField(max_length=15, blank=True)
    eduLang = models.CharField(max_length=15, blank=True)
    eduType = models.CharField(max_length=15, blank=True)
    paymentForm = models.CharField(max_length=50, blank=True)
    studentStatus = models.CharField(max_length=20, blank=True)
    image = models.TextField(null=True, blank=True)
    birth_date = models.CharField(max_length=10, null=True, blank=True)
    passport_pin = models.CharField(max_length=15, null=True, blank=True)
    passport_number = models.CharField(max_length=10, null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    is_student = models.BooleanField(default=True)
    is_leader = models.BooleanField(default=False)



    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def hashing_password(self):
        pass

    def save(self, *args, **kwargs):
        if not self.pk and not self.password.startswith('pbkdf2_sha256'):
            self.password = make_password(self.password)
        
        # super() metod orqali asosiy saqlash metodini chaqirish
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"