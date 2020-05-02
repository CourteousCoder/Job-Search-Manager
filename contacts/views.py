from django.shortcuts import render
from datetime import datetime


def index(request):
    contacts_list = [
        {'name': 'Fan Sina', 'company': 'Workbridge', 'last_interaction': datetime.now(),
         'next_follow_up': datetime.now()},
        {'name': 'John Sina', 'company': 'Workbridge', 'last_interaction': datetime.now(),
         'next_follow_up': datetime.now()},
        {'name': 'Casn Sina', 'company': 'Workbridge', 'last_interaction': datetime.now(),
         'next_follow_up': datetime.now()},
        {'name': 'Dan Sina', 'company': 'Workbridge', 'last_interaction': datetime.now(),
         'next_follow_up': datetime.now()},
        {'name': 'Bam Sina', 'company': 'Workbridge', 'last_interaction': datetime.now(),
         'next_follow_up': datetime.now()},
    ]
    context = dict(contacts_list=contacts_list)
    return render(request, "contacts/index.html", context=context)
