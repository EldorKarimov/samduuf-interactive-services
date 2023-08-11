from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext_lazy as _

from accounts.models import Student

class Leader(models.Model):
    leader = models.OneToOneField(Student, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='media/leader/image')
    position = models.CharField(verbose_name=_('Position'), max_length=128)
    detail_link = models.TextField()

    class Meta:
        verbose_name_plural = _('Leaders')

    def __str__(self):
        return f"{self.leader.first_name} {self.leader.last_name}"
    

class Appeal(models.Model):
    TYPE_APPLICATION = (
        (None, "Tanlang"),
        ('taklif', 'taklif'),
        ('shikoyat', 'shikoyat'),
        ('apellatsiya', 'apellatsiya')
    )
    leader = models.ForeignKey(Leader, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    message = models.TextField()
    theme = models.CharField(max_length=128)
    file_upload = models.FileField(upload_to='upload/path/', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'pdf', 'docx', 'pptx'])], null=True, blank=True)
    type_application = models.CharField(max_length=15, choices=TYPE_APPLICATION)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_checked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.leader.leader.first_name} {self.leader.leader.last_name}"
    
class Answer(models.Model):
    message = models.TextField()
    student_id = models.CharField(max_length=15)
    leader = models.CharField(max_length=128)

    def __str__(self):
        return self.student_id