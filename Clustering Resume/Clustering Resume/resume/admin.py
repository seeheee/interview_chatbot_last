from django.contrib import admin
from .models import Resume
from .models import MBTI, All

# Register your models here.
admin.site.register(Resume)
admin.site.register(MBTI)
admin.site.register(All)