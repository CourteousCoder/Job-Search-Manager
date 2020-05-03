from django.db import models
from django.urls import reverse


class Company(models.Model):
    RECRUITER = 'REC'
    EMPLOYER = 'EMP'
    name = models.CharField(max_length=255, blank=False)
    type = models.CharField(max_length=3, null=False, blank=False, choices=[
        (RECRUITER, 'Recruiting Agency'),
        (EMPLOYER, 'Potential Employer'),
    ], default=EMPLOYER)
    website = models.URLField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('contacts:company_detail', kwargs=dict(pk=self.pk))

    def __str__(self):
        type = self.get_type_display()
        name = self.name
        return f'{name} ({type})'

    class Meta:
        verbose_name_plural = 'companies'


class Person(models.Model):
    company = models.ForeignKey(Company, null=True, on_delete=models.SET_NULL)
    jobs = models.ManyToManyField('jobs.Job', through='contacts.Interaction')
    name = models.CharField(max_length=100, blank=False, verbose_name="full name")
    phone_number = models.CharField(max_length=14, null=True)
    email_address = models.EmailField(null=True)
    linked_in_profile = models.URLField(null=True, verbose_name='LinkedIn profile URL')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def last_interaction(self):
        return self.interaction_set.latest()

    def get_absolute_url(self):
        return reverse('contacts:person_detail', kwargs=dict(pk=self.pk))

    def __str__(self):
        name = self.name
        company = self.company
        return f'{name} from {company}'

    class Meta:
        verbose_name_plural = 'people'


class Interaction(models.Model):
    person = models.ForeignKey(Person, null=True, on_delete=models.SET_NULL)
    job = models.ForeignKey('jobs.Job', null=True, on_delete=models.SET_NULL)
    notes = models.TextField(null=True)
    follow_up_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        person = self.person
        job = self.job
        time = self.created_at.isoformat()
        if person is not None and job is not None:
            return f'{time} - {person} about {job}'
        elif person is not None:
            return f'{time} - {person}'
        elif job is not None:
            return f'{time} - {job}'
        else:
            return f'{time} (orphaned)'

    class Meta:
        get_latest_by = 'created_at'
