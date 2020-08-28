from django.views.generic import TemplateView, FormView
from django.shortcuts import get_object_or_404

from central_balkan.dashboard.models import SlideShowImage, Question
from central_balkan.dashboard.forms import AskQuestionForm

from central_balkan.products.models import Category, Product


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


class AskQuestionView(FormView):
    form_class = AskQuestionForm

    def get_success_url(self):
        return self.request.META['HTTP_REFERER']

    def form_valid(self, form):
        product = Product.objects.get(id=form.cleaned_data['product'])

        Question.objects.create(
            email=form.cleaned_data['email'],
            message=form.cleaned_data['message'],
            product=product,
        )

        return super().form_valid(form)
