from django.urls import path
from djangocourse.apps import DjangocourseConfig
from djangocourse.views import *

app_name = DjangocourseConfig.name

urlpatterns = [
    path('', DistributionListView.as_view(), name='distribution'),
    path('client/', ClientListView.as_view(), name='client'),
    path('client_create/', ClientCreateView.as_view(), name='client_create'),
    path('client_update/<int:pk>/', ClientUpdateView.as_view(), name='client_update'),
    path('client_delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),
    path('message/', MessageListView.as_view(), name='message'),
    path('message_create/', MessageCreateView.as_view(), name='message_create'),
    path('message_update/<int:pk>/', MessageUpdateView.as_view(), name='message_update'),
    path('message_delete/<int:pk>/', MessageDeleteView.as_view(), name='message_delete'),
    path('distribution_create/', DistributionCreateView.as_view(), name='distribution_create'),
    path('distribution_update/<int:pk>/', DistributionUpdateView.as_view(), name='distribution_update'),
    path('distribution_delete/<int:pk>/', DistributionDeleteView.as_view(), name='distribution_delete'),
]
