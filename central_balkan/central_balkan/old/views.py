from django.views.generic import TemplateView


class OldTemplateView(TemplateView):
    def get_template_names(self):
        template_name = self.kwargs.get('template_name')

        return 'old_site/{template_name}'.format(
            template_name=template_name
        )
