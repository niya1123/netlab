from django.shortcuts import render

# Create your views here.
def top(request):
    """
    topページ.
    """
    template_name = 'sns_app/index.html'