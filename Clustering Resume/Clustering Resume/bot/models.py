from django.db import models
from django.conf import settings
from resume.models import Resume

class QuestionList(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    author = models.CharField('작성자', max_length=16, null=False, default='')
    my_resume = models.ForeignKey(Resume, on_delete=models.CASCADE, null=True, related_name='pk')
    my_resume = models.IntegerField(default=0)
    question1 = models.TextField('질문1', default='')
    question2 = models.TextField('질문2', default='')
    question3 = models.TextField('질문3', default='')
    question4 = models.TextField('질문4', default='')
    question5 = models.TextField('질문5', default='')
    question6 = models.TextField('질문6', default='')
    question7 = models.TextField('질문7', default='')
    question8 = models.TextField('질문8', default='')
    question9 = models.TextField('질문9', default='')
    question10 = models.TextField('질문10', default='')
    question11 = models.TextField('질문11', default='')
    question12 = models.TextField('질문12', default='')
    question13 = models.TextField('질문13', default='')
    question14 = models.TextField('질문14', default='')
    question15 = models.TextField('질문15', default='')
    question16 = models.TextField('질문16', default='')
    question17 = models.TextField('질문17', default='')
    question18 = models.TextField('질문18', default='')
    question19 = models.TextField('질문19', default='')
    question20 = models.TextField('질문20', default='')
    answer1 = models.TextField('답변1', default='')
    answer2 = models.TextField('답변2', default='')
    answer3 = models.TextField('답변3', default='')
    answer4 = models.TextField('답변4', default='')
    answer5 = models.TextField('답변5', default='')
    answer6 = models.TextField('답변6', default='')
    answer7 = models.TextField('답변7', default='')
    answer8 = models.TextField('답변8', default='')
    answer9 = models.TextField('답변9', default='')
    answer10 = models.TextField('답변10', default='')
    answer11 = models.TextField('답변11', default='')
    answer12 = models.TextField('답변12', default='')
    answer13 = models.TextField('답변13', default='')
    answer14 = models.TextField('답변14', default='')
    answer15 = models.TextField('답변15', default='')
    answer16 = models.TextField('답변16', default='')
    answer17 = models.TextField('답변17', default='')
    answer18 = models.TextField('답변18', default='')
    answer19 = models.TextField('답변19', default='')
    answer20 = models.TextField('답변20', default='')

    answer_alltext = models.TextField('전체답변', default='')
    word = models.TextField('단어', default="")
    word_count =models.TextField('단어 갯수', default="")

    mbti = models.TextField(max_length=32, default="")
    mbti1 = models.TextField(max_length=32, default="")
    mbti2 = models.TextField(max_length=32, default="")
    famous = models.TextField(max_length=32, default="")
    answer_mbti_E = models.FloatField('E', default=0)
    answer_mbti_I = models.FloatField('I', default=0)
    answer_mbti_N = models.FloatField('N', default=0)
    answer_mbti_S = models.FloatField('S', default=0)
    answer_mbti_T = models.FloatField('T', default=0)
    answer_mbti_F = models.FloatField('F', default=0)
    answer_mbti_J = models.FloatField('J', default=0)
    answer_mbti_P = models.FloatField('P', default=0)

class TestQuestionList(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    author = models.CharField('작성자', max_length=16, null=False, default='')
    my_resume = models.ForeignKey(Resume, on_delete=models.CASCADE, null=True, related_name='pk')
    my_resume = models.IntegerField(default=0)
    question1 = models.TextField('질문1', default='')
    question2 = models.TextField('질문2', default='')
    question3 = models.TextField('질문3', default='')
    question4 = models.TextField('질문4', default='')
    question5 = models.TextField('질문5', default='')
    question6 = models.TextField('질문6', default='')
    answer1 = models.TextField('답변1', default='')
    answer2 = models.TextField('답변2', default='')
    answer3 = models.TextField('답변3', default='')
    answer4 = models.TextField('답변4', default='')
    answer5 = models.TextField('답변5', default='')
    answer6 = models.TextField('답변6', default='')