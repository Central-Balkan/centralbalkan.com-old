from django.views.generic import TemplateView

from central_balkan.dashboard.models import SlideShowImage


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
