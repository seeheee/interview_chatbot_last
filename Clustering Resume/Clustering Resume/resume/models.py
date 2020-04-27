from django.conf import settings
from django.db import models
from django.utils import timezone


class Resume(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    author = models.CharField('작성자', max_length=16, null=False)
    title = models.CharField(max_length=200, verbose_name="제목")
    motive = models.TextField(verbose_name="본 회사의 지원동기를 작성해주시기 바랍니다.", help_text=u"본인이 생각하는 본 회사의 장단점과 자신의 장단점을 비교하여 작성해주시기 바랍니다.")
    dream = models.TextField(verbose_name="입사 후 포부를 작성해주시기 바랍니다.", help_text=u"앞으로의 목표 및 계획을 구체적으로 작성해주시기 바랍니다.")
    growth = models.TextField(verbose_name="본인의 성장과정을 작성해주시기 바랍니다.", help_text=u"현재의 가치관을 가지게 된 계기와 원칙이 있다면 그러한 생각을 갖게 된 과정을 작성해주시기 바랍니다.")
    pac = models.TextField(verbose_name="본인의 장점과 단점을 작성해주시기 바랍니다.", help_text=u"자신의 장점이 어떠한 차별성을 갖고 있는지, 자신의 단점은 어떻게 개선중인지 작성해주시기 바랍니다.")
    activities = models.TextField(verbose_name="참여했던 대외활동, 공모전, 프로젝트 경험을 작성해주시기 바랍니다.", help_text=u"경험했던 활동에 대한 소개와 깨달은점과 배운점 위주로 작성해주시기 바랍니다.")

    score1 = models.FloatField('적극적', default=0) #실수타입으로 점수 반영
    score2 = models.FloatField('열정적', default=0)
    score3 = models.FloatField('성실성', default=0)
    score4 = models.FloatField('책임감', default=0)
    score5 = models.FloatField('사교적', default=0)
    score6 = models.FloatField('신중함', default=0)

    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class All(models.Model):
    all = models.TextField('전체자소서', default="")
    word = models.TextField('단어', default="")
    word_count = models.TextField('단어 갯수', default="")

class Propensity(models.Model):
    score1 = models.FloatField('적극적', default=0) #실수타입으로 점수 반영
    score2 = models.FloatField('열정적', default=0)
    score3 = models.FloatField('성실성', default=0)
    score4 = models.FloatField('책임감', default=0)
    score5 = models.FloatField('사교적', default=0)
    score6 = models.FloatField('신중함', default=0)


class MBTI(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    author = models.CharField('작성자', max_length=20, null=False)
    my_resume = models.ForeignKey(Resume, on_delete=models.CASCADE, null=True, related_name='pk')
    my_resume = models.IntegerField(default=0)
    E = models.FloatField('E', default=0)
    I = models.FloatField('I', default=0)
    N = models.FloatField('N', default=0)
    S = models.FloatField('S', default=0)
    T = models.FloatField('T', default=0)
    F = models.FloatField('F', default=0)
    J = models.FloatField('J', default=0)
    P = models.FloatField('P', default=0)
    text = models.TextField(max_length=64, default="")
    mbti1 = models.TextField(max_length=32, default="")
    mbti2 = models.TextField(max_length=1024, default="")
    Ambti1 = models.TextField(max_length=32, default="")
    Ambti2 = models.TextField(max_length=1024, default="")
    textEI = models.TextField(max_length=1024, default="")
    textSN = models.TextField(max_length=1024, default="")
    textTF = models.TextField(max_length=1024, default="")
    textJP = models.TextField(max_length=1024, default="")
    textfinal = models.TextField(max_length=64, default="")
    result = models.CharField(max_length=10, default='')