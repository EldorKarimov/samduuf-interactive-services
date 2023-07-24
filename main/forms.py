from django import forms
from .models import Appeal, Answer, Leader

class AppealForm(forms.ModelForm):
    class Meta:
        model = Appeal
        fields = ['leader', 'message', 'file_upload']

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        exclude = ['message']