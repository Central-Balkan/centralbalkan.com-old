from django.db import models

from django.conf import settings

from central_balkan.common.utils import get_domain


class SlideShowImage(models.Model):
    class Meta:
        verbose_name = "Снимка за началната страница"
        verbose_name_plural = "Снимки за началната страница"

    image = models.ImageField(
        'Изображение',
        upload_to='initial_page_slideshow/',
        blank=True,
        null=True
    )

    @property
    def image_url(self):
        domain = get_domain()
        media_url = settings.MEDIA_URL

        return '{domain}{media_url}{image}'.format(
            domain=domain,
            media_url=media_url,
            image=self.image
        )

    def __str__(self):
        return 'Снимка за начална страница ({image})'.format(
            image=self.image
        )
