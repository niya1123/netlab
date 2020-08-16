# from django.urls import reverse_lazy
# from django.views import generic

# from ..accounts.views import OnlyYouMixin
# from .forms import CreateContentFrom
# from .models import Content

# class CreateContentView(OnlyYouMixin, generic.CreateView):
#     """コンテンツ作成ビュー"""
#     model = Content
#     from_class = CreateContentFrom
#     template_name = 'contents/create_content.html'
#     success_url = reverse_lazy('contents:create_content_done')
