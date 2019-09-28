from django.conf import settings
from django.contrib.sites.models import Site

from rest_framework import serializers


def create_serializer_class(name, fields):
    return type(name, (serializers.Serializer, ), fields)


def inline_serializer(*, fields, data=None, **kwargs):
    serializer_class = create_serializer_class(name='', fields=fields)

    if data is not None:
        return serializer_class(data=data, **kwargs)

    return serializer_class(**kwargs)


def get_domain():
    current_site = Site.objects.get(pk=settings.SITE_ID)
    http_protocol = settings.HTTP_PROTOCOL

    return '%s://%s' % (http_protocol, current_site.domain)
