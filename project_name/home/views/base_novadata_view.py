from django.views.generic import TemplateView


class BaseNovadataView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["breadcrumb"] = self.get_breadcrumb()
        return context

    def get_breadcrumb(self):
        return []
