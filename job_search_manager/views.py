from django.shortcuts import redirect
from django.urls import reverse


def landing(request):
    return redirect(reverse('contacts:person_list'))
