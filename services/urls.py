from django.urls import path
from services.views import (
    ServiceListView,
    ServiceDetailView,
    MechanicServiceManageView,
    MechanicServiceDetailView,
)

urlpatterns = [
    path('list/', ServiceListView.as_view(), name='service_list'),
    path('<int:pk>/', ServiceDetailView.as_view(), name='service_detail'),
    path('manage/', MechanicServiceManageView.as_view(), name='mechanic_manage_services'),
    path('manage/create/', MechanicServiceDetailView.as_view(), name='create_service'),
    path('manage/<int:pk>/', MechanicServiceDetailView.as_view(), name='mechanic_manage_service'),
]
