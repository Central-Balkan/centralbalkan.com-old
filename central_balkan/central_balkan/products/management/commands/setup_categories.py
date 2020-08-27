from django.core.management.base import BaseCommand

from central_balkan.products.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = {
            'partners': 'Партньори',
            'fences': 'Огради',
            'doors': 'Врати',
            'stairs': 'Стълби',
            'metal-constructions': 'Метални конструкции',
            'garden-furniture': 'Градински мебели',
            'sheds': 'Навеси',
            'parapets': 'Парапети',
            'metal-details': 'Детайли от метал',
        }

        for slub, name in categories.items():
            Category.objects.get_or_create(slug=slub, name=name)
