from django.db import models


class Company(models.Model):
    RECRUITER = 'REC'
    EMPLOYER = 'EMP'
    name = models.CharField(max_length=255, blank=False)
    type = models.CharField(max_length=3, blank=False, choices=[
        (RECRUITER, 'Recruiting Agency'),
        (EMPLOYER, 'Potential Employer'),
    ])
    website = models.URLField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'companies'


class Person(models.Model):
    company = models.ForeignKey(Company, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100, blank=False, verbose_name="full name")
    phone_number = models.CharField(max_length=14, null=True)
    email_address = models.EmailField(null=True)
    linked_in_profile = models.URLField(null=True, verbose_name='LinkedIn profile URL')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'people'


class Interaction(models.Model):
    person = models.ForeignKey(Person, null=True, on_delete=models.SET_NULL)
    job = models.ForeignKey('jobs.Job', null=True, on_delete=models.SET_NULL)
    notes = models.TextField(null=True)
    follow_up_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
