from django.db import models


class Job(models.Model):
    company_name = models.CharField(max_length=120)
    company_email = models.EmailField(max_length=60, unique=True)
    job_title = models.CharField(max_length=120)
    job_description = models.TextField(blank=True)
    salary = models.IntegerField()
    city = models.CharField(max_length=60)
    state = models.CharField(max_length=60)
    created_on = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f'{ self.company_name } { self.job_title } { self.salary }'
