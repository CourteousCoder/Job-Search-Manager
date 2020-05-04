from django.views.generic import ListView, CreateView, UpdateView, DetailView
from .models import Job


class JobList(ListView):
    model = Job


class JobDetail(DetailView):
    model = Job


class JobCreate(CreateView):
    model = Job
    fields = [
        'title',
        'company',
        'status',
        'description',
    ]


class JobUpdate(UpdateView):
    model = Job
    fields = [
        'title',
        'company',
        'status',
        'description',
    ]
