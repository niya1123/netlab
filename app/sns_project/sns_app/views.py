from django.views import generic

# Create your views here.
class Top(generic.TemplateView):
    """
    topページ.
    """
    template_name = 'sns_app/index.html'