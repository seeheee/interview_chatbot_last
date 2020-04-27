from django import forms
from .models import Introduces
from django.utils.translation import gettext_lazy as _
from user.models import User

class ResumeForm(forms.Form):
    model = Introduces
    motive = forms.CharField(required=True, label='본 회사의 지원동기를 작성해주시기 바랍니다.', widget=forms.Textarea(attrs={'placeholder':'본인이 생각하는 본 회사의 장단점과 자신의 장단점을 비교하여 작성해주시기 바랍니다.'}))
    dream = forms.CharField(required=True, label='입사 후 포부를 작성해주시기 바랍니다.', widget=forms.Textarea(attrs={'placeholder':'앞으로의 목표 및 계획을 구체적으로 작성해주시기 바랍니다.'}))
    growth = forms.CharField(required=True, label='본인의 성장과정을 작성해주시기 바랍니다.', widget=forms.Textarea(attrs={'placeholder':'현재의 가치관을 가지게 된 계기와 원칙이 있다면 그러한 생각을 갖게 된 과정을 작성해주시기 바랍니다.'}))
    PAC = forms.CharField(required=True, label='본인의 장점과 단점을 작성해주시기 바랍니다.', widget=forms.Textarea(attrs={'placeholder': '자신의 장점이 어떠한 차별성을 갖고 있는지, 자신의 단점은 어떻게 개선중인지 작성해주시기 바랍니다.'}))
    activities = forms.CharField(required=True, label='참여했던 대외활동, 공모전, 프로젝트 경험을 작성해주시기 바랍니다.', widget=forms.Textarea(attrs={'placeholder': '경험했던 활동에 대한 소개와 깨달은점과 배운점 위주로 작성해주시기 바랍니다.'}))
