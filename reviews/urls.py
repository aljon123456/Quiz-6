from django.urls import path
from .views import CreateServiceReviewView, GetServiceReviewsView

urlpatterns = [
    path('service/<int:service_id>/review/', CreateServiceReviewView.as_view(), name='create_review'),
    path('service/<int:service_id>/reviews/', GetServiceReviewsView.as_view(), name='get_reviews'),
]
