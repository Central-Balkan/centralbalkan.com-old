import os

from django.core.management.base import BaseCommand
from django.conf import settings

from central_balkan.dashboard.models import SlideShowImage


class Command(BaseCommand):
    def handle(self, *args, **options):
        # SlideShowImage
        media_folder = '{}/'.format(settings.MEDIA_ROOT)
        images_path = SlideShowImage.image.field.upload_to
        images_for_slideshow = os.listdir(
            '{}{}'.format(
                media_folder,
                images_path
            )
        )

        for image in images_for_slideshow:
            SlideShowImage.objects.create(
                image=image
            )
