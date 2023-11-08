from typing import Any, Optional
from django import forms
from django.contrib.auth.base_user import AbstractBaseUser
from .models import Student
from .api import HemisApi
from main.models import Leader
from django.contrib.auth.forms import PasswordChangeForm
from django.utils.translation import gettext_lazy as _
from datetime import datetime

class StudentRegisterForm(forms.Form, HemisApi):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=128, widget=forms.PasswordInput())
    

    def save(self):
        user_data = self.user_data_json(self.cleaned_data['username'], self.cleaned_data['password'])

        if user_data == 'error':
            return None
    
        student = Student.objects.create(
            username = int(user_data.get('data').get('student_id_number')),
            first_name = user_data.get('data').get('first_name'),
            last_name = user_data.get('data').get('second_name'),
            third_name = user_data.get('data').get('third_name'),
            full_name = user_data.get('data').get('full_name'),
            email = user_data.get('data').get('email'),
            phone = user_data.get('data').get('phone'),
            student_id_number = int(user_data.get('data').get('student_id_number')),
            university = user_data.get('data').get('university'),
            faculty = user_data.get('data').get('faculty').get('name'),
            group = user_data.get('data').get('group').get('name'),
            specialty = user_data.get('data').get('specialty').get('name'),
            occommodation = user_data.get('data').get('accommodation').get('name'),
            district = user_data.get('data').get('district').get('name'),
            address = user_data.get('data').get('address'),
            eduForm = user_data.get('data').get('educationForm').get('name'),
            eduLang = user_data.get('data').get('educationLang').get('name'),
            eduType = user_data.get('data').get('educationType').get('name'),
            paymentForm = user_data.get('data').get('paymentForm').get('name'),
            studentStatus = user_data.get('data').get('studentStatus').get('name'),
            image = user_data.get('data').get('image'),
            birth_date = str(datetime.fromtimestamp(user_data.get('data').get('birth_date')).date()),
            passport_pin = user_data.get('data').get('passport_pin'),
            passport_number = user_data.get('data').get('passport_number'),
            gender = user_data.get('data').get('gender').get('name'),
            country = user_data.get('data').get('country').get('name'),
        )
        student.set_password(self.cleaned_data['password'])
        student.save()
        return student
    
class LeaderProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = (
            'full_name',
            'birth_date', 
            'gender',
            'phone',
            'email',
            'address',
            'country'
        )

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label=_("Eski parolni kiriting")
    )

    new_password1 = forms.CharField(
        label=_("Yangi parol kiriting")
    )

    new_password2 = forms.CharField(
        label=_("Yangi parolni qaytadan kiriting")
    )

    def clean_new_password2(self) -> str:
        new_password1 = self.cleaned_data.get('new_password1')
        new_password2 = self.cleaned_data.get('new_password2')

        if new_password1 and new_password2 and new_password1 != new_password2:
            raise forms.ValidationError(_("Ikkita yangi parol maydoni mos kelmadi."))

        return super().clean_new_password2()
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['new_password1'].help_text = _("Parolingiz kamida 8 ta belgidan iborat boʻlishi kerak, shaxsiy maʼlumotlaringizga juda oʻxshash boʻlmasligi, tez-tez ishlatiladigan parol boʻlmasligi va butunlay raqamli boʻlishi mumkin emas.")
