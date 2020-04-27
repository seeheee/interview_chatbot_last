from django import forms
from .models import Resume
from django.utils.translation import gettext_lazy as _

class ResumeForm(forms.ModelForm):

    class Meta:
        model = Resume
        fields = ('title', 'motive', 'dream', 'growth', 'pac', 'activities')