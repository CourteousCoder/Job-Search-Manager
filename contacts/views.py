from django.views.generic import ListView, CreateView, UpdateView, DetailView

from contacts.forms import PersonForm
from contacts.models import Person


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
