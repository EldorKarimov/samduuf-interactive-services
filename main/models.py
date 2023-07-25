from django.db import models
from django.core.validators import FileExtensionValidator

from accounts.models import Student

class Leader(models.Model):
    leader = models.OneToOneField(Student, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='media/leader/image')

    def __str__(self):
        return f"{self.leader.first_name} {self.leader.last_name}"
    
    def get_full_name(self):
        return f"{self.leader.first_name} {self.leader.last_name}" 

class Appeal(models.Model):
    leader = models.ForeignKey(Leader, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    message = models.TextField()
    file_upload = models.FileField(upload_to='upload/path/', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'pdf', 'docx', 'pptx'])], null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.leader.leader.first_name} {self.leader.leader.last_name}"
    
class Answer(models.Model):
    message = models.TextField()
    student_id = models.CharField(max_length=15)
    leader = models.CharField(max_length=128)

    def __str__(self):
        return self.student_id