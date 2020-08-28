from django.contrib import admin

from central_balkan.dashboard.models import SlideShowImage, Question


@admin.register(SlideShowImage)
class SlideShowImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'image_url')


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_at',
        'updated_at',
        'email',
        'message',
        'product',
        'answered',
    )
