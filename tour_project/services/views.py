from django.views.generic import ListView, DetailView
from .models import Service


class ServicesListView(ListView):
    model = Service
    template_name = 'services/list.html'
    context_object_name = 'services'

    def get_queryset(self):
        # Фильтрация услуг, где страна активна, с использованием select_related и prefetch_related
        return Service.objects.filter(country__is_active=True).select_related('country').prefetch_related('images')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        services_with_images = []
        for service in context['services']:
            image = service.images.first()  # Получаем первое изображение
            services_with_images.append({
                'service': service,
                'image': image
            })
        context['services_with_images'] = services_with_images
        return context


class ServiceDetailView(DetailView):
    model = Service
    template_name = 'services/detail.html'
    context_object_name = 'service'

    def get_queryset(self):
        # Используйте prefetch_related для изображений
        return super().get_queryset().prefetch_related('images')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        service = context['service']
        images = service.images.all()  # Получаем все изображения услуги
        context['images'] = images
        return context
