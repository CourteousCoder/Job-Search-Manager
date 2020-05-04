from django.urls import path
from jobs.views import *

app_name = 'jobs'
urlpatterns = [
    path('', JobList.as_view(), name='job_list'),
    path('new', JobCreate.as_view(), name='job_create'),
    path('<pk>', JobDetail.as_view(), name='job_detail'),
    path('<pk>/edit', JobUpdate.as_view(), name='job_update'),
]
