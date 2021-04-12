from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.conf import settings


from .validators import ASCIIUsernameValidator


# Create your models here.
class Faculty(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "faculties"

    def __str__(self):
        return self.name
    

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Project(models.Model):
    topic = models.CharField(max_length=500)
    student_name = models.CharField(max_length=500)
    year = models.DateField()
    supervisor_name = models.CharField(max_length=500)
    faculty = models.ForeignKey(Faculty, on_delete=models.PROTECT)
    darpartment = models.ForeignKey(Department, on_delete=models.PROTECT)
    document = models.FileField(upload_to="documents/", blank=False, null=False)

    def get_document(self):
        return self.document.url

    def __str__(self):
        return self.topic

class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    # phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    # phone = models.CharField(validators=[phone_regex], max_length=15, blank=True, null=True)
    picture = models.ImageField(upload_to="pictures/", blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    username_validator = ASCIIUsernameValidator()

    def get_picture(self):
        no_picture = settings.STATIC_URL + 'assets/img/img_avatar.png'
        try:
            return self.picture.url
        except:
            return no_picture

    def get_full_name(self):
        full_name = self.username
        if self.first_name and self.last_name:
            full_name = self.first_name + " " + self.last_name
        return full_name


