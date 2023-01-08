from django.views.generic import View


class BaseNovadataView(View):
    need_breadcrumb = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["breadcrumb"] = self.get_breadcrumb()
        return context

    def get_breadcrumb(self):
        if self.need_breadcrumb:
            name = self.__class__.__name__
            raise NotImplementedError(
                f"A classe {name} não implementou os breadcrumbs. Caso não seja necessário, sete a variável need_breadcrumb para False."
            )
        else:
            return []
