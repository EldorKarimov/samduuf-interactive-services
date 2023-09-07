from django import forms
from .models import Appeal, Answer, Leader
from django.utils.translation import gettext_lazy as _
from ckeditor.widgets import CKEditorWidget

class AppealForm(forms.ModelForm):
    file_upload = forms.FileField(required=False)
    leader = forms.ModelChoiceField(queryset=Leader.objects.all(), empty_label=_("tanlang"))
    is_checked = forms.BooleanField(required=True)
    message = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Appeal
        fields = ['leader', 'type_application', 'theme', 'message', 'file_upload', 'is_checked']
    

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        exclude = ['appeal', 'leader', 'student_id']