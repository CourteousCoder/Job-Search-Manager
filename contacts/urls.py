from django.urls import path

from contacts.views import *

app_name = 'contacts'

urlpatterns = [
    path('people', PersonList.as_view(), name='person_list'),
    path('people/new', PersonCreate.as_view(), name='person_create'),
    path('people/<pk>', PersonDetail.as_view(), name='person_detail'),
    path('people/<pk>/edit', PersonUpdate.as_view(), name='person_update'),
    path('companies', CompanyList.as_view(), name='company_list'),
    path('companies/new', CompanyCreate.as_view(), name='company_create'),
    path('companies/<pk>', CompanyDetail.as_view(), name='company_detail'),
    path('companies/<pk>/edit', CompanyUpdate.as_view(), name='company_update'),
    path('interactions/new', InteractionCreate.as_view(), name='interaction_create'),
    path('interactions/<pk>', InteractionDetail.as_view(), name='interaction_detail'),
    path('interactions/<pk>/edit', InteractionUpdate.as_view(), name='interaction_update'),
]
