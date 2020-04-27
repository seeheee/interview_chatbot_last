from django.contrib import admin
from .models import Personality, Activity, Growth, Other

# Register your models here.
admin.site.register(Activity)
admin.site.register(Growth)
admin.site.register(Personality)
admin.site.register(Other)