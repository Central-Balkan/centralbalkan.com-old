from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404

from central_balkan.dashboard.models import SlideShowImage
from central_balkan.products.models import Category


class MainPageView(TemplateView):
    template_name = 'dashboard/main_page.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['images'] = [
            {
                'idx': idx,
                'url': image.image_url,
                'active_class': 'active' if idx == 0 else ''

            }
            for idx, image in enumerate(SlideShowImage.objects.all())
        ]

        return context


class CategoryDetailView(TemplateView):
    template_name = 'dashboard/category_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        category = get_object_or_404(
            Category.objects.prefetch_related('products'),
            slug=self.kwargs['category_slug']
        )

        context['category'] = category

        return context
