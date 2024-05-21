from django.db import models
from django.urls import reverse


class StudentDetail(models.Model):
    gender_choices = [('M', 'Male'), ('F', 'Female')]
    gender = models.CharField(choices=gender_choices, max_length=1,
                              default=None, null=True)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    student_id = models.SlugField(max_length=250, unique=True)
    fathers_name = models.CharField(max_length=250)
    mothers_name = models.CharField(max_length=250)
    dob = models.DateTimeField()
    objects = models.Manager() # The default manager.
    std_choices = [('1', 'I'), ('2', 'II'), ('3', 'III'), ('4', 'IV'),
                   ('5', 'V'), ('6', 'VI'), ('7','VII'),
                   ('8', 'VIII'), ('9', 'IX'), ('10', 'X')]
    std = models.CharField(choices=std_choices, max_length=2, default=None, null=True)

    class Meta:
        verbose_name_plural = "Student Details"

    def get_absolute_url(self):
        return reverse('student:view@StudentDetails', args=[self.student_id])