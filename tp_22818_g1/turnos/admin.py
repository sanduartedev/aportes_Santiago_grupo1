from django.contrib import admin
from .models import Choice, Question
#noticia
from .models import Noticia

admin.site.register(Noticia)
#fin 

#Faq
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    fields = ["pub_date", "question_text"]
    inlines = [ChoiceInline]
    list_display = ("question_text", "pub_date")
    list_filter = ["pub_date"]
    search_fields = ["question_text"]

admin.site.register(Question, QuestionAdmin)
#FIN Faq