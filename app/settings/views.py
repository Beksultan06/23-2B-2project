from django.shortcuts import render
from app.settings.models import Settings
from django.views.generic import TemplateView

# Create your views here.
# def index(request):
#     settings_id = Settings.objects.latest("id")
#     return render(request, 'base/index.html', locals())

class IndexView(TemplateView):
    template_name = 'base/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['settings_id'] = Settings.objects.latest("id")
        return context

class ContactView(TemplateView):
    template_name = 'base/contact.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)