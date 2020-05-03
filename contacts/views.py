from django.views.generic import ListView, CreateView, UpdateView, DetailView

from contacts.forms import PersonForm, CompanyForm
from contacts.models import Person, Company


class PersonList(ListView):
    model = Person


class PersonDetail(DetailView):
    model = Person


class PersonCreate(CreateView):
    form_class = PersonForm
    model = Person


class PersonUpdate(UpdateView):
    form_class = PersonForm
    model = Person


class CompanyList(ListView):
    model = Company


class CompanyDetail(DetailView):
    model = Company


class CompanyCreate(CreateView):
    form_class = CompanyForm
    model = Company


class CompanyUpdate(UpdateView):
    form_class = CompanyForm
    model = Company
