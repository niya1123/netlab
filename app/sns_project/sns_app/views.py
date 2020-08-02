from django.shortcuts import render

# Create your views here.
def top(request):
    """
    topページ.
    """
    ctx={'title': 'LearnSNS'}
    return render(request, 'sns_app/index.html', ctx)