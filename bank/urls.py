from django.urls import path
from .views import IfscDetails, BranchDetails

urlpatterns = [
    path('ifsc/', IfscDetails.as_view(), name='bankdetails'),
    path('branch/', BranchDetails.as_view(), name='branchdetails')
]
