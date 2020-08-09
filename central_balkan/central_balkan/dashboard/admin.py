from django.contrib import admin

from central_balkan.dashboard.models import SlideShowImage


@admin.register(SlideShowImage)
class SlideShowImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'image_url')
