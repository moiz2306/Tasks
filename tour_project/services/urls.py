from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import ServicesListView, ServiceDetailView

app_name = 'services'

urlpatterns = [
    path('', ServicesListView.as_view(), name='services_list'),
    path('<int:pk>/', ServiceDetailView.as_view(), name='service_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
