from django.db import models


class Employeemodel(models.Model):
    GENDER_CHOICE = [
        ('M','Male'),
        ('F','FeMale'),
    ]
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30,blank=True)
    email_id=models.EmailField(max_length=30)
    phone_num=models.IntegerField()
    employee_gender=models.CharField(choices=GENDER_CHOICE,max_length=1)
    employee_address=models.TextField()
    employee_jobs=models.ManyToManyField('Availablejobs')
    date_of_birth=models.DateField()


class Availablejobs(models.Model):
    name=models.CharField(max_length=30)
    #employee_jobs=models.ManyToManyField(Employeemodel,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


