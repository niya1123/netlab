from django.contrib import admin
from .models import ROOT, EL, SEL, SSEL, QuestionTemplate
# Register your models here.

admin.site.register(ROOT)
admin.site.register(EL)
admin.site.register(SEL)
admin.site.register(SSEL)
admin.site.register(QuestionTemplate)