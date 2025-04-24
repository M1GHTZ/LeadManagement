from django.urls import path
from api import views

urlpatterns=[
    path('lead/',views.LeadView.as_view()),
    path('lead/<int:pk>/',views.LeadRetrieveUpdateDestroyView.as_view())
]