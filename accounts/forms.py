from django import forms
from .models import Student
from .api import HemisApi

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
            image = user_data.get('data').get('image')
        )
        student.set_password(self.cleaned_data['password'])
        student.save()
        return student