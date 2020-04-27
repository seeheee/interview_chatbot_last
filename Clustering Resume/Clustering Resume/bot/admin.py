from django.contrib import admin
from .models import QuestionList, TestQuestionList

# Register your models here.
admin.site.register(QuestionList)
admin.site.register(TestQuestionList)