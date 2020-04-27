from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from resume.models import Propensity, Resume, MBTI
from user.models import User
from question.models import Personality, Activity, Growth, Other
from .models import QuestionList, TestQuestionList
from konlpy.tag import Twitter
from collections import Counter

import operator
import json
import random


# Create your views here.
count = 0
questions = []
testque = []
qlist = []
list_final = []
activity_randoms = []
growth_randoms = []
# Every interview contents
interview_contents = []
ran_num = 0
activity_major_count = 0
mbti_score = [0, 0, 0, 0, 0, 0, 0, 0]  # E, I, S, N, T, F, J, P 순서

def home(request):
    return HttpResponse('HelloWorld')


def bot(request):
    del questions[:]
    del testque[:]
    del qlist[:]
    del list_final[:]
    del interview_contents[:]
    global user
    user = request.user
    if user.my_resume == 0 or user.my_mbti == "":
        mbtis = MBTI.objects.all()
        return render(request, 'mbti_test.html', {'mbtis': mbtis})
    else:
        print(user)
        return render(request, 'bot.html')


def chatbot(request):
    return render(request, 'chatbot.html')


def chatbot_cam(request):
    return render(request, 'cam.html')


def stopwatch(request):
    return render(request, 'stopwatch.html')


def button_real(request):
    return render(request, 'button_real.html')


def mypage(request):
    return render(request, 'home/mypage.html')


def gan(request):
    return render(request, 'gan.html')


def logo(request):
    return render(request, 'logo.html')


def mirime(request):
    return render(request, 'mirime.html')


def bottom(request):
    return render(request, 'bottom.html')


def soundwave(request):
    return render(request, 'soundwave.html')




@csrf_exempt
def get_interview(request):
    my_resume = User.objects.get(email=user).my_resume  # user의 resume id를 가져옴
    mbti = MBTI.objects.get(my_resume=my_resume)
    resume = Resume.objects.get(pk=my_resume)  # 해당 resume을 가져옴
    global count, ran_num, activity_major_count, mbti_score  # 전체 질문 전역역변 (총 20개까지)
    global questions, qlist, list_final, activity_randoms, growth_randoms, interview_contents
    num = []

    if count == 0:
        # print(propensity)
        # 활동 질문 3개
        del questions[:]
        del testque[:]
        del qlist[:]
        del list_final[:]
        del interview_contents[:]

        req = json.loads(request.body)
        param = req.get('queryResult').get('parameters').get('major')
        # print(req)

        if param == "비전공자입니다":
            activity_major = Activity.objects.filter(title='others')
            activity_major_count = Activity.objects.filter(title='others').count()
            ran_num = random.randint(0, activity_major_count - 1)
        else:
            activity_major = Activity.objects.filter(title='major_intelligence')
            activity_major_count = Activity.objects.filter(title='major_intelligence').count()
            ran_num = random.randint(0, activity_major_count - 1)

        for i in range(3):
            while ran_num in num:
                ran_num = random.randint(0, activity_major_count - 1)
            num.append(ran_num)

        for i in num:
            questions.append(activity_major[i].question)

        # 활동의 랜덤 질문 1개
        # for activity in resume:
        #     activity = activity.activities
        activity = resume.activities

        circle = ['동아리']
        competition = ['공모전']
        development = ['개발']
        english = ['영어']
        intern = ['인턴']
        overseas = ['어학연수', '해외', '연수', '여행']
        school = ['학교']
        volunteer = ['봉사', '봉사활동']
        major = ['전공', '부전공']

        if any(format in activity for format in intern):
            activity_randoms.append('intern')
        if any(format in activity for format in overseas):
            activity_randoms.append('overseas')
        if any(format in activity for format in competition):
            activity_randoms.append('competition')
        if any(format in activity for format in development):
            activity_randoms.append('development')
        if any(format in activity for format in circle):
            activity_randoms.append('circles')
        if any(format in activity for format in volunteer):
            activity_randoms.append('volunteer')
        if any(format in activity for format in school):
            activity_randoms.append('school')
        if any(format in activity for format in english):
            activity_randoms.append('english')
        if any(format in activity for format in major):
            activity_randoms.append('major')

        print(activity_randoms)

        if not activity_randoms:
            activity_other = Activity.objects.filter(title='others')
            activity_other_count = Activity.objects.filter(title='others').count()
        else:
            activity_random = random.choice(activity_randoms)  # 있다면 random으로 choice
            activity_other = Activity.objects.filter(title=activity_random)
            activity_other_count = Activity.objects.filter(title=activity_random).count()
            print(activity_random)

        ran_num = random.randint(0, activity_other_count)
        questions.append(activity_other[ran_num].question)

        # 성장과정 1개
        resume_growth = resume.growth

        family = ['가족', '오빠', '형', '언니', '누나', '엄마', '아빠', '어머니', '어머님', '아버님', '아버지', '할머니', '할아버지', '동생', '형제',
                  '자매']
        environment = ['환경']

        if any(format in resume_growth for format in family):
            growth_randoms.append('family')
        if any(format in resume_growth for format in environment):
            growth_randoms.append('environment')

        if not growth_randoms:
            growth_other = Growth.objects.filter(title='others')
            growth_other_count = Growth.objects.filter(title='others').count()
        else:
            growth_random = random.choice(growth_randoms)
            growth_other = Growth.objects.filter(title=growth_random)
            growth_other_count = Growth.objects.filter(title=growth_random).count()
            print(growth_random)

        ran_num = random.randint(0, growth_other_count - 1)
        questions.append(growth_other[ran_num].question)

        # 지원동기
        reson_text = "지원 동기를 짧게 요약해 말해보세요."
        questions.append(reson_text)
        testque.append(reson_text)

        # 포부
        hope_text = "입사 이후의 포부에 대해 말해보세요."
        questions.append(hope_text)
        testque.append(hope_text)

        test_growth = Growth.objects.filter(title='test')
        test_growth_count = Growth.objects.filter(title='test').count()
        ran_nums = random.randint(0, test_growth_count - 1)
        testque.append(test_growth[ran_nums].question)

        # 성향 랜덤 2개
        personality_random = Personality.objects.filter(title='random')
        personality_random_count = Personality.objects.filter(title='random').count()
        ran_num = random.randint(0, personality_random_count - 1)
        num = []
        for i in range(2):
            while ran_num in num:
                ran_num = random.randint(0, personality_random_count - 1)
            num.append(ran_num)

        for i in range(2):
            questions.append(personality_random[num[i]].question)

        mbti_score[0] = mbti.E
        mbti_score[1] = mbti.I
        mbti_score[2] = mbti.N
        mbti_score[3] = mbti.S
        mbti_score[4] = mbti.T
        mbti_score[5] = mbti.F
        mbti_score[6] = mbti.J
        mbti_score[7] = mbti.P

        print(mbti_score)

        pb = {}  # 각 차이 저장
        pb['ei'] = abs(float(mbti_score[0]) - float(mbti_score[1]))
        pb['sn'] = abs(float(mbti_score[2]) - float(mbti_score[3]))
        pb['tf'] = abs(float(mbti_score[4]) - float(mbti_score[5]))
        pb['jp'] = abs(float(mbti_score[6]) - float(mbti_score[7]))

        print(pb)

        # 가장 차이가 큰 성향 3개
        sort_pb = sorted(pb.items(), key=operator.itemgetter(1), reverse=True)  # 큰거부터 작은거(내림차순)

        print(sort_pb)

        print(sort_pb[0][0])
        personality_first = Personality.objects.filter(title=sort_pb[0][0])
        personality_first_count = personality_first.count()

        ran_num = random.randint(0, personality_first_count - 1)
        num = []

        testque.append(personality_first[ran_nums].question)

        for i in range(3):
            while ran_num in num:
                ran_num = random.randint(0, personality_first_count - 1)
            num.append(ran_num)

        for i in num:
            questions.append(personality_first[i].question)

        # 가장 차이가 작은 성향 2개
        print(sort_pb[3][0])
        personality_low = Personality.objects.filter(title=sort_pb[3][0])
        personality_low_count = personality_low.count()

        ran_num = random.randint(0, personality_low_count - 1)
        num = []

        testque.append(personality_low[ran_nums].question)

        for i in range(2):
            while ran_num in num:
                ran_num = random.randint(0, personality_low_count - 1)
            num.append(ran_num)

        for i in num:
            questions.append(personality_low[i].question)

        # 차이가 큰 성향의 경우 판단 질문 2개
        if sort_pb[0][0] == "ei":
            if mbti_score[0] > mbti_score[1]:
                mbti_text1 = "외향적인면은 가지셨지만 내향적인 부분은 부족하신것 같은데 이런점이 단점이 된적은 없었나요?"
            else:
                mbti_text1 = "내향적인면은 가지셨지만 외향적인 부분은 부족하신것 같은데 이런점이 단점이 된적은 없었나요?"
        elif sort_pb[0][0] == "sn":
            if mbti_score[3] > mbti_score[2]:
                mbti_text1 = "감각적인면은 가지셨지만 직관적인 부분은 부족하신것 같은데 이런점이 단점이 된적은 없었나요?"
            else:
                mbti_text1 = "직관적인면은 가지셨지만 감각적인 부분은 부족하신것 같은데 이런점이 단점이 된적은 없었나요?"
        elif sort_pb[0][0] == "tf":
            if mbti_score[4] > mbti_score[5]:
                mbti_text1 = "사고적인면은 가지셨지만 감정적인 부분은 부족하신것 같은데 이런점이 단점이 된적은 없었나요?"
            else:
                mbti_text1 = "감정적인면은 가지셨지만 사고적인 부분은 부족하신것 같은데 이런점이 단점이 된적은 없었나요?"
        elif sort_pb[0][0] == "jp":
            if mbti_score[6] > mbti_score[7]:
                mbti_text1 = "판단적인면은 가지셨지만 인식적인 부분은 부족하신것 같은데 이런점이 단점이 된적은 없었나요?"
            else:
                mbti_text1 = "인식적인면은 가지셨지만 판단적인 부분은 부족하신것 같은데 이런점이 단점이 된적은 없었나요?"

        mbti_text2 = "부족한 성향을 보완하기 위해 노력해본 경험이 있나요?"

        questions.append(mbti_text1)
        questions.append(mbti_text2)

        # 차이가 작은 성향의 경우 판단 질문 2개
        if sort_pb[3][0] == "ei":
            mbti_text3 = "외향성과 내향성 모두 갖고 계신거같은데 좀 더 되고자 하거나 선호하는 성향은 어느쪽이신가요?"
            mbti_text4 = "외향성과 내향성 중 무엇이 더 본인에게 좋은 영향을 준다고 생각하나요?"
        elif sort_pb[3][0] == "sn":
            mbti_text3 = "감각형과 직관형을 모두 갖고 계신거같은데 좀 더 되고자 하거나 선호하는 성향은 어느쪽이신가요?"
            mbti_text4 = "감각형과 직관형 중 무엇이 더 본인에게 좋은 영향을 준다고 생각하나요?"
        elif sort_pb[3][0] == "tf":
            mbti_text3 = "사고형과 감정형을 모두 갖고 계신거같은데 좀 더 되고자 하거나 선호하는 성향은 어느쪽이신가요?"
            mbti_text4 = "사고형과 감정형 중 무엇이 더 본인에게 좋은 영향을 준다고 생각하나요?"
        elif sort_pb[3][0] == "jp":
            mbti_text3 = "판단형과 인식형을 모두 갖고 계신거같은데 좀 더 되고자 하거나 선호하는 성향은 어느쪽이신가요?"
            mbti_text4 = "판단형과 인식형 중 무엇이 더 본인에게 좋은 영향을 준다고 생각하나요?"

        questions.append(mbti_text3)
        questions.append(mbti_text4)

        # 완전 랜덤 2개
        other = Other.objects.filter(title='random')
        other_count = Other.objects.filter(title='random').count()
        ran_num = random.randint(0, other_count - 1)
        num = []

        for i in range(1):
            while ran_num in num:
                ran_num = random.randint(0, other_count - 1)
            num.append(ran_num)

        for i in range(1):
            testque.append(other[num[i]].question)

        for i in range(2):
            while ran_num in num:
                ran_num = random.randint(0, other_count - 1)
            num.append(ran_num)

        for i in range(2):
            questions.append(other[num[i]].question)

        # 모의면접 끝
        final_text = "수고하셨습니다. 면접 종료하기 버튼을 눌러 자신의 면접 결과를 확인하세요!"
        testque.append(final_text)

        print(questions)
        print(len(questions))

        print(testque)
        print(len(testque))

        # list = []
        ran_num = 0

        for i in range(7):
            while ran_num in qlist:
                ran_num = random.randint(0, 6)
            qlist.append(ran_num)
        print(qlist)

        for i in range(7):
            qlist[i]
            if qlist[i] == 0:
                for j in range(4):
                    # list_final.append(questions[j])
                    list_final.append(questions[j])
            elif qlist[i] == 1:
                # list_final.append(questions[4])
                list_final.append(questions[4])
            elif qlist[i] == 2:
                # list_final.append(questions[5])
                list_final.append(questions[5])
            elif qlist[i] == 3:
                # list_final.append(questions[6])
                list_final.append(questions[6])
            elif qlist[i] == 4:
                for j in range(7, 9):
                    # list_final.append(questions[j])
                    list_final.append(questions[j])
            elif qlist[i] == 5:
                for j in range(9, 18):
                    # list_final.append(questions[j])
                    list_final.append(questions[j])
            elif qlist[i] == 6:
                for j in range(18, 20):
                    # list_final.append(questions[j])
                    list_final.append(questions[j])

        list_final.append(final_text)
        print(len(list_final))
        print(list_final)

    count = (count) % len(questions)
    counts = (count) % len(testque)
    # fulfillmentText = {'fulfillmentText': list_final[count]}
    fulfillmentText = {'fulfillmentText': testque[counts]}

    if count == len(list_final) - 1:
        count = 0
    else:
        count += 1

    # Every interview contents
    req = json.loads(request.body)
    # get contexts from json
    answer = req.get('queryResult').get('queryText')
    # get parameters from json
    param = req.get('queryResult').get('parameters')
    print(answer)
    interview_contents.append(answer)

    if answer == "끝":
        count = 0
        print(count)
        fulfillmentText = "초기화하겠습니다."
        return JsonResponse(fulfillmentText, safe=True)

    # if len(interview_contents) == 21:
    #     Que = QuestionList()
    #
    #     Que.author = user
    #     Que.my_resume = resume.pk
    #     Que.question1 = questions[0]
    #     Que.question2 = questions[1]
    #     Que.question3 = questions[2]
    #     Que.question4 = questions[3]
    #     Que.question5 = questions[4]
    #     Que.question6 = questions[5]
    #     Que.question7 = questions[6]
    #     Que.question8 = questions[7]
    #     Que.question9 = questions[8]
    #     Que.question10 = questions[9]
    #     Que.question11 = questions[10]
    #     Que.question12 = questions[11]
    #     Que.question13 = questions[12]
    #     Que.question14 = questions[13]
    #     Que.question15 = questions[14]
    #     Que.question16 = questions[15]
    #     Que.question17 = questions[16]
    #     Que.question18 = questions[17]
    #     Que.question19 = questions[18]
    #     Que.question20 = questions[19]
    #
    #     Que.answer1 = interview_contents[1]
    #     Que.answer2 = interview_contents[2]
    #     Que.answer3 = interview_contents[3]
    #     Que.answer4 = interview_contents[4]
    #     Que.answer5 = interview_contents[5]
    #     Que.answer6 = interview_contents[6]
    #     Que.answer7 = interview_contents[7]
    #     Que.answer8 = interview_contents[8]
    #     Que.answer9 = interview_contents[9]
    #     Que.answer10 = interview_contents[10]
    #     Que.answer11 = interview_contents[11]
    #     Que.answer12 = interview_contents[12]
    #     Que.answer13 = interview_contents[13]
    #     Que.answer14 = interview_contents[14]
    #     Que.answer15 = interview_contents[15]
    #     Que.answer16 = interview_contents[16]
    #     Que.answer17 = interview_contents[17]
    #     Que.answer18 = interview_contents[18]
    #     Que.answer19 = interview_contents[19]
    #     Que.answer20 = interview_contents[20]

    if len(interview_contents) == 7:
        Que = QuestionList()
        Quet = TestQuestionList()

        Quet.author = user
        Quet.my_resume = resume.pk
        Quet.question1 = testque[0]
        Quet.question2 = testque[1]
        Quet.question3 = testque[2]
        Quet.question4 = testque[3]
        Quet.question5 = testque[4]
        Quet.question6 = testque[5]

        Quet.answer1 = interview_contents[1]
        Quet.answer2 = interview_contents[2]
        Quet.answer3 = interview_contents[3]
        Quet.answer4 = interview_contents[4]
        Quet.answer5 = interview_contents[5]
        Quet.answer6 = interview_contents[6]

        # Que.answer_alltext ="결과다"
        #
        # interview_length = len(interview_contents)
        # for i in range(interview_length):
        #     Que.answer_alltext += interview_contents[i]
        #     i += 1
        #
        # print(Que.answer_alltext)
        #
        # nlpy = Twitter()
        # nouns = nlpy.nouns(Que.answer_alltext)
        # print(nouns)
        #
        # count = Counter(nouns)
        # tag_count = []
        # tags = []
        #
        # for n, c in count.most_common(100):
        #     dics = {'tag': n, 'count': c}
        #     if len(dics['tag']) >= 2 and len(tags) <= 49:
        #         tag_count.append(dics)
        #         tags.append(dics['tag'])
        #
        # for tag in tag_count:
        #     print(" {:<14}".format(tag['tag']), end='\t')
        #     print("{}".format(tag['count']))
        #
        # Que.word = tag
        # Que.word_count = tag_count
        #
        # print("\n---------------------------------")
        # print("     명사 총  {}개".format(len(tags)))
        # print("---------------------------------\n\n")

        dic = {
            'E': ['책임감', '관리', '해결', '열정', '역량', '참여', '직접', '활동', '정열', '외부', '사람', '행동', '모임', '공동체', '공적',
                  '말', '토론', '외향성', '대인관계', '사교', '적극성', '경험', '스스로', '적극', '도전', ],
            'I': ['생각', '이해', '경험', '집중', '장소', '도서관', '개인', '사적', '숲', '내향성', '깊이', '대인관계', '유지', '자기', '내부',
                  '부활동', '신중', '글', '서서히'],
            'S': ['실제', '나무', '사실', '감각', '경험', '지금', '현재', '초점', '정확', '처리', '관찰', '생산', '보존', '거북이', '오감', '의존',
                  '중시', '사건', '묘사', '경향', '추수', '함'],
            'N': ['가능성', '숲', '미래', '신속', '처리', '상상력', '이론', '디자인', '통찰', '변화', '토끼', '직관', '육감', '영감', '의존', '지향',
                  '의미', '추구', '초점', '아이디어', '비유', '암시', '묘사', '경향'],
            'T': ['진실', '논리', '분석', '사실', '관심', '정의', '머리', '관성', '질서', '공평', '사고', '객관', '판단', '원리', '원칙', '규범',
                  '기준', '중시', '지적', '논평', '신뢰'],
            'F': ['팀원', '긍정', '관계', '관심', '상황', '의미', '자비', '가슴', '열정', '재치', '조화', '가치', '친절', '중심', '감정', '사람과',
                  '정상', '참작', '설명', '사람', '영향', '포괄', '나', '우호', '협조', '친구', '배려', '도움', '사랑'],
            'J': ['개발', '프로젝트', '기획', '준비', '설계', '계획', '조직', '방향', '과단성', '집중', '일', '지배인', '결과', '판단', '목적', '목표',
                  '기한', '엄수', '사전', '체계', '정리', '정돈', '의지', '추진', '결론', '통제', '조정', '목적의식', '감각', '기준', '자기', '의사',
                  '신뢰'],
            'P': ['의견', '융통', '과정', '목적', '방향', '변화', '상황', '개방', '자유', '호기심', '즉흥', '질문', '놀이', '기업가', '시작', '인식',
                  '일정', '자율', '융통성', '이해', '수용', '적응', '재량', '처리']}

        dic_sum = {
            'ENFJ': ['사람', '생각', '의견', '외교', '충성', '경향', '적극', '책임감', '사교성', '사교', '참을성', '관심', '동선', '대체로', '동의',
                     '현재', '미래', '가능성', '추구', '능란', '계획', '제시', '집단', '능력', '교직', '성직', '심리', '상담', '치료', '예술',
                     '문학', '판매', '맹목', '대해', '자기', '이상', '개인', '언어', '표현', '성적', '열정', '염려', '지적', '마음'],
            'ENFP': ['일', '열성', '재능', '창의', '관심', '사람', '통찰', '정열', '활기', '상상력', '정적', '항상', '가능성', '시도', '문제해결',
                     '수행', '능력', '도움', '상담', '교육', '과학', '저널리스트', '광고', '판매', '성직', '작가', '분야', '반복', '일상', '창의력',
                     '요구', '흥미', '호기심', '성적', '재주', '자발', '표현', '독립', '우호', '열정', '상상', '활동'],
            'ENTJ': ['계획', '감정', '통솔력', '결정', '관심', '논리', '필요', '자신', '열성', '단호', '지도력', '활동', '장기', '안목', '선호',
                     '지식', '욕구', '지적', '자극', '아이디어', '처리', '준비', '분석', '조직', '체계', '추진', '의견', '귀', '타인', '느낌',
                     '인정', '판단', '결론', '피해', '누적', '크게', '폭발', '가능성', '전략', '비판', '조절', '도전', '직선', '객관', '이론'],
            'ENTP': ['일', '문제', '능력', '독창', '안목', '다방면', '관심', '재능', '도전', '분석', '이론', '창의력', '상상력', '시도', '솔선',
                     '논리', '해결', '사람', '동향', '대해', '일상', '세부', '경시', '즉', '흥미', '수행', '가지', '발명가', '과학자', '해결사',
                     '저널리스트', '마케팅', '컴퓨터', '등', '때', '경쟁', '현실', '더', '편이', '진취', '독립', '전략', '창의', '융통성', '자원'],
            'ESFJ': ['사람', '이야기', '요구', '마음', '양심', '관심', '협력', '동료', '능동', '구성원', '정리정돈', '참을성', '행동', '교직', '성직',
                     '판매', '필요', '간호', '의료', '일이', '대한', '문제', '입장', '반대', '의견', '자신', '거절', '상처', '충성', '사교', '개인',
                     '협동', '재치', '감동', '전통', '동정'],
            'ESFP': ['사교', '수용', '낙천', '실제', '사람', '일', '상식', '분야', '활동', '현실', '상황', '주위', '관심', '사물', '사실', '물질',
                     '소유', '운동', '실생활', '능력', '필요', '의료', '판매', '교통', '유흥', '간호', '비서', '사무직', '감독', '기계', '수다',
                     '깊이', '마무리', '경향', '조직체', '공동체', '분위기', '조성', '역할', '성적', '융통성', '우호', '표현', '협동', '관용', '개방'],
            'ESTJ': ['현실', '조직', '일', '능력', '분야', '사실', '지도력', '행정', '체계', '결정', '경향', '구체', '활동', '실질', '감각', '계획',
                     '추진', '기계', '재능', '업체', '조직체', '지도자', '목표', '설정', '지시', '이행', '결과', '사업가', '관리', '생산', '건축',
                     '발휘', '속단', '속결', '업무', '사람', '인간', '중심', '가치', '타인', '감정', '고려', '미래', '가능성', '현재', '추구',
                     '실용', '논리', '효율', '객관', '실제', '구조', '인적'],
            'ESTP': ['현실', '사실', '개방', '일', '별로', '문제해결', '적응력', '관용', '사람', '선입관', '감각', '협책', '모색', '문제', '해결',
                     '능력', '적응', '친구', '설명', '운동', '음식', '활동', '주로', '보고', '생활', '순발력', '기억', '예술', '멋', '판단력',
                     '연장', '재료', '논리', '분석', '처리', '추상', '아이디어', '개념', '대해', '흥미', '행동', '지향', '융통성', '재미', '재주',
                     '열정', '낙천', '자발', '실용', '설득'],
            'INFJ': ['분야', '직관', '통찰', '열정', '인내심', '양심', '화합', '추구', '창의력', '말', '타인', '영향력', '독창', '성과', '내적',
                     '독립심', '신념', '자신', '영감', '구현', '정신', '지도자', '사람', '중심', '가치', '중시', '성직', '심리학', '심리치료', '상담',
                     '예술', '문학', '테크니컬', '순수과학', '연구', '개발', '시도', '대한', '열성', '경향', '목적', '달성', '주변', '조건', '경시',
                     '갈등', '내적인', '생활', '소유', '내면', '반응', '남', '공유', '헌신', '창의', '깊이', '결심', '개념', '전체', '이상'],
            'INFP': ['자신', '경향', '정열', '신념', '이상', '일', '인간', '능력', '헌신', '목적', '낭만', '내적', '마음', '관계', '일이', '사람',
                     '책임감', '지향', '남', '지배', '인상', '거의', '완벽', '주의', '노동', '대가', '흥미', '자하', '이해', '복지', '기여', '언어',
                     '문학', '상담', '심리학', '과학', '예술', '분야', '발휘', '현실', '실제', '상황', '고려', '융통성', '모험심', '창의', '깊이',
                     '과묵', '공감'],
            'INTJ': ['독창', '타인', '사고', '비판', '분석', '직관', '자신', '목적', '능력', '노력', '분야', '창의력', '내적', '신념', '행동',
                     '영감', '실현', '의지', '결단', '인내심', '중요시', '달성', '시간', '일', '통찰', '활용', '과학', '엔지니어링', '발명', '정치',
                     '철학', '발휘', '일과', '사람', '그대로', '사실', '감정', '고려', '관점', '독립', '논리', '체계', '마음', '전이', '이론',
                     '기준', '객관', '전체'],
            'INTP': ['논리', '지적', '과묵', '분석', '관심', '호기심', '추상', '문제', '해결', '하나', '대해', '말', '이해', '직관', '통찰', '재능',
                     '개인', '인관', '관계', '친목', '잡담', '객관', '비평', '발휘', '순수과학', '연구', '수학', '엔지니어링', '개념', '경제', '철학',
                     '심리학', '학문', '비현실적', '사교성', '결여', '경향', '자신', '능력', '은근', '과시', '때문', '회의', '초연', '이론', '독립',
                     '사색', '독창', '자율', '자기', '결정'],
            'ISFJ': ['헌신', '자신', '타인', '책임감', '처리', '조직', '정적', '인내력', '다른', '사람', '사정', '고려', '감정', '현실', '감각',
                     '실제', '경험', '통해', '인정', '난관', '밀고', '의존', '독창', '요구', '표현', '관심', '관찰', '분야', '의료', '간호', '교직',
                     '사무직', '사회사업', '일', '대처', '행동', '분별', '상세', '전통', '참을성', '봉사', '보호', '매우', '동정'],
            'ISFP': ['말', '적응력', '관용', '자신', '의견', '타인', '융통성', '연기력', '속마음', '상대방', '동정', '자기', '능력', '성격', '유형',
                     '가장', '가치', '강요', '충돌', '피하', '중시', '인간', '관계', '일', '감정', '결정', '추진', '일상', '활동', '개방', '협동',
                     '충성', '신뢰', '자발', '이해'],
            'ISTJ': ['조직', '집중', '분별', '실제', '사실', '체계', '일', '발휘', '기억', '처리', '책임감', '현실', '감각', '보수', '경향', '문제',
                     '해결', '과거', '경험', '적용', '반복', '일상', '대한', '인내력', '자신', '타인', '감정', '기분', '배려', '전체', '타협',
                     '방안', '고려', '노력', '정확성', '선호', '회계', '법률', '생산', '건축', '의료', '사무직', '관리직', '능력', '위기', '상황',
                     '안정', '신뢰', '확고', '부동', '의무'],
            'ISTP': ['상황', '능력', '객관', '사실', '인생', '관찰', '파악', '도구', '형', '이상', '발휘', '조직', '기계', '과묵', '절제', '호기심',
                     '민감', '성과', '말', '필요', '자신', '일과', '관계', '인간관계', '직접', '가을', '에너지', '소비', '사람', '자료', '정리',
                     '인과관계', '원리', '관심', '연장', '재능', '법률', '경제', '마케팅', '판매', '통계', '분야', '느낌', '감정', '타인', '대한',
                     '마음', '표현', '편의', '실제', '실적', '응용', '독립', '모험', '융통성', '자기', '결정']}

        bow = {'E': 0, 'I': 0, 'S': 0, 'N': 0, 'T': 0, 'F': 0, 'J': 0, 'P': 0}
        bow_sum = {'E': 0, 'I': 0, 'S': 0, 'N': 0, 'T': 0, 'F': 0, 'J': 0, 'P': 0}

        for_mbti_text = ''
        for i in range(7):  # 원래 21개
            for_mbti_text += interview_contents[i]

        spliter = Twitter()
        for_mbti_text = spliter.nouns(for_mbti_text)

        for key in dic.keys():
            for voca in for_mbti_text:
                if voca in dic[key]:
                    bow[key] += 1
            bow[key] = bow[key] / len(dic[key])

        for key in dic_sum.keys():
            for voca in for_mbti_text:
                if voca in dic_sum[key]:
                    for i in range(0, 4):
                        bow_sum[key[i:i + 1]] += 1
            for i in range(0, 4):
                bow_sum[key[i:i + 1]] = bow_sum[key[i:i + 1]] / len(dic_sum[key])

        mbti_sum = {'E': 0, 'I': 0, 'S': 0, 'N': 0, 'T': 0, 'F': 0, 'J': 0, 'P': 0}
        sum = 0

        for key in mbti_sum.keys():
            mbti_sum[key] = bow[key] + bow_sum[key]

        for key in mbti_sum.keys():
            sum += mbti_sum[key]
        sum /= 8

        for key in mbti_sum.keys():
            mbti_sum[key] += sum

        mbti_type = list(mbti_sum.keys())
        mbti_best_type = {}

        for i in range(0, 4):
            key = mbti_type[2 * i] if mbti_sum[mbti_type[2 * i]] > mbti_sum[mbti_type[2 * i + 1]] else mbti_type[
                2 * i + 1]
            tmp = {key: abs(mbti_sum[mbti_type[2 * i]] - mbti_sum[mbti_type[2 * i + 1]])}
            print(tmp)
            mbti_best_type.update(tmp)
            tmp.clear()

        print("\nSum Of Every Score")
        print(mbti_sum)

        result = []
        i = 1
        tmp = 0
        for key in mbti_sum.keys():
            tmp += float(mbti_sum[key])
            if i % 2 == 0:
                result.append(tmp)
                tmp = 0
            i += 1

        k = 0
        for key in mbti_sum.keys():
            mbti_sum[key] = round((float(mbti_sum[key]) / result[k // 2]) * 100, 1)
            k += 1

        print("Percentage Of MBTI and Resume")
        print(mbti_sum)

        Que.answer_mbti_E = mbti_sum['E']
        Que.answer_mbti_I = mbti_sum['I']
        Que.answer_mbti_N = mbti_sum['N']
        Que.answer_mbti_S = mbti_sum['S']
        Que.answer_mbti_T = mbti_sum['T']
        Que.answer_mbti_F = mbti_sum['F']
        Que.answer_mbti_J = mbti_sum['J']
        Que.answer_mbti_P = mbti_sum['P']

        my_org_type = list(mbti_best_type.keys())
        print("my_org_type :" + "".join(my_org_type) + "\n")

        my_1st_type = "".join(my_org_type)  # 나의 답변 MBTI

        print("my_1st_type :" + my_1st_type)

        # 자기소개서 성향에 대한 정보 보여주기 위한 부분
        if my_1st_type == "INTJ":
            mbti1 = "용의주도한 전략가(INTJ)"
            mbti2 = "윗자리에 있는 사람은 고독한 법, 전략적 사고에 뛰어나며 매우 극소수인 건축가형 사람은 이를 누구보다 뼈저리게 이해합니다. 전체 인구의 2%에 해당하는 이들은 유독 여성에게서는 더욱 찾아보기 힘든 유형으로, 인구의 단 0.8%를 차지합니다. 체스를 두는 듯한 정확하고 계산된 움직임과 풍부한 지식을 소유하고 있는 이들은 그들과 견줄 만한 비슷한 부류의 사람을 찾는 데 종종 어려움을 겪습니다. 건축가형 사람은 상상력이 풍부하면서도 결단력이 있으며, " + "야망이 있지만 대외적으로 표현하지 않으며, 놀랄 만큼 호기심이 많지만 쓸데없는 데 에너지를 낭비하는 법이 없습니다."
            famous = "Colin Powell / Elon Musk / Michelle Obama / Tywin Lannister"
        elif my_1st_type == "INTP":
            mbti1 = "논리적인 사색가(INTP)"
            mbti2 = "사색가형은 전체 인구의 3% 정도를 차지하는 꽤 흔치 않은 성격 유형으로, 이는 그들 자신도 매우 반기는 일입니다. 왜냐하면, 사색가형 사람보다 '평범함'을 거부하는 이들이 또 없기 때문입니다. 이 유형의 사람은 그들이 가진 독창성과 창의력, 그리고 그들만의 독특한 관점과 왕성한 지적 호기심에 나름의 자부심을 가지고 있습니다. 보통 철학자나 사색가, 혹은 몽상에 빠진 천재 교수로도 많이 알려진 이들은 역사적으로 수많은 과학적 발전을 이끌어 내기도 하였습니다."
            famous = "Bill Gates / Ellen Page / Blaise Pascal / Issac Newton"
        elif my_1st_type == "ENTJ":
            mbti1 = "대담한 통솔자(ENTJ)"
            mbti2 = "통솔자형 사람은 천성적으로 타고난 리더입니다. 이 유형에 속하는 사람은 넘치는 카리스마와 자신감으로 공통의 목표 실현을 위해 다른 이들을 이끌고 진두지휘합니다. 예민한 성격의 사회운동가형 사람과 달리 이들은 진취적인 생각과 결정력, 그리고 냉철한 판단력으로 그들이 세운 목표 달성을 위해 가끔은 무모하리만치 이성적 사고를 하는 것이 특징입니다. 이들이 인구의 단 3%에 지나지 않는 것이 어쩌면 다행일 수도 있습니다. 그렇지 않으면 인구 대다수를 차지하는 소심하고 섬세한 성향의 사람들이 모두 주눅 들어 살지도 모르니까요. 단, 평소 잊고 살기는 하나 우리 삶을 윤택하게 해주는 위대한 사업가나 기관을 이끄는 통솔자형 사람들이 있음에 다행이기도 합니다."
            famous = "Steve Jobs / Jim Carrey / Malcolm X / David Palmer"
        elif my_1st_type == "ENTP":
            mbti1 = "뜨거운 논쟁을 즐기는 변론가(ENTP)"
            mbti2 = "변론가형 사람은 타인이 믿는 이념이나 논쟁에 반향을 일으킴으로써 군중을 선동하는 일명 선의의 비판자입니다. 결단력 있는 성격 유형이 논쟁 안에 깊이 내재한 숨은 의미나 상대의 전략적 목표를 꼬집기 위해 논쟁을 벌인다고 한다면, 변론가형 사람은 단순히 재미를 이유로 비판을 일삼습니다. 아마도 이들보다 논쟁이나 정신적 고문을 즐기는 성격 유형은 없을 것입니다. 이는 천부적으로 재치 있는 입담과 풍부한 지식을 통해 논쟁의 중심에 있는 사안과 관련한 그들의 이념을 증명해 보일 수 있기 때문입니다."
            famous = "Adam Savage / Jim Halpert / The Joker / Irene Adler"
        elif my_1st_type == "INFJ":
            mbti1 = "선의의 옹호자(INFJ)"
            mbti2 = "선의의 옹호자형은 가장 흔치 않은 성격 유형으로 인구의 채 1%도 되지 않습니다. 그럼에도 불구하고 나름의 고유 성향으로 세상에서 그들만의 입지를 확고히 다집니다. 이들 안에는 깊이 내재한 이상향이나 도덕적 관념이 자리하고 있는데, 다른 외교형 사람과 다른 점은 이들은 단호함과 결단력이 있다는 것입니다. 바라는 이상향을 꿈꾸는데 절대 게으름 피우는 법이 없으며, 목적을 달성하고 지속적으로 긍정적인 영향을 미치고자 구체적으로 계획을 세워 이행해 나갑니다."
            famous = "Goethe / Morgan Freeman / Marie Kondo / Lady Gaga"
        elif my_1st_type == "INFP":
            mbti1 = "열정적인 중재자(INFP)"
            mbti2 = "중재자형 사람은 최악의 상황이나 악한 사람에게서도 좋은 면만을 바라보며 긍정적이고 더 나은 상황을 만들고자 노력하는 진정한 이상주의자입니다. 간혹 침착하고 내성적이며 심지어는 수줍음이 많은 사람처럼 비추어지기도 하지만, 이들 안에는 불만 지피면 활활 타오를 수 있는 열정의 불꽃이 숨어있습니다. 인구의 대략 4%를 차지하는 이들은 간혹 사람들의 오해를 사기도 하지만, 일단 마음이 맞는 사람을 만나면 이들 안에 내재한 충만한 즐거움과 넘치는 영감을 경험할 수 있을 것입니다."
            famous = "Julia Roberts / Alicia Keys / Tom Hiddleston / Johnny Depp"
        elif my_1st_type == "ENFJ":
            mbti1 = "정의로운 사회운동가(ENFJ)"
            mbti2 = "사회운동가형 사람은 카리스마와 충만한 열정을 지닌 타고난 리더형입니다. 인구의 대략 2%가 이 유형에 속하며, 정치가나 코치 혹은 교사와 같은 직군에서 흔히 볼 수 있습니다. 이들은 다른 이들로 하여금 그들의 꿈을 이루며, 선한 일을 통하여 세상에 빛과 소금이 될 수 있도록 사람들을 독려합니다. 또한, 자신뿐 아니라 더 나아가 살기 좋은 공동체를 만들기 위해 사람들을 동참시키고 이끄는 데에서 큰 자부심과 행복을 느낍니다."
            famous = "Barack Obama / Oprah Winfrey / John Cusack / Ben Affleck"
        elif my_1st_type == "ENFP":
            mbti1 = "재기발랄한 활동가(ENFP)"
            mbti2 = "활동가형 사람은 자유로운 사고의 소유자입니다. 종종 분위기 메이커 역할을 하기도 하는 이들은 단순한 인생의 즐거움이나 그때그때 상황에서 주는 일시적인 만족이 아닌 타인과 사회적, 정서적으로 깊은 유대 관계를 맺음으로써 행복을 느낍니다. 매력적이며 독립적인 성격으로 활발하면서도 인정이 많은 이들은 인구의 대략 7%에 속하며, 어느 모임을 가든 어렵지 않게 만날 수 있습니다."
            famous = "Robert Downey / Jr.Robin Williams / Will Smith"
        elif my_1st_type == "ISTJ":
            mbti1 = "청렴결백한 논리주의자(ISTJ)"
            mbti2 = "논리주의자형은 가장 다수의 사람이 속하는 성격 유형으로 인구의 대략 13%를 차지합니다. 청렴결백하면서도 실용적인 논리력과 헌신적으로 임무를 수행하는 성격으로 묘사되기도 하는 이들은, 가정 내에서뿐 아니라 법률 회사나 법 규제 기관 혹은 군대와 같이 전통이나 질서를 중시하는 조직에서 핵심 구성원 역할을 합니다. 이 유형의 사람은 자신이 맡은 바 책임을 다하며 그들이 하는 일에 큰 자부심을 가지고 있습니다. 또한, 목표를 달성하기 위해 시간과 에너지를 허투루 쓰지 않으며, 이에 필요한 업무를 정확하고 신중하게 처리합니다."
            famous = "Sting, Angela Merkel / Natalie Portman / Natalie Portman"
        elif my_1st_type == "ISFJ":
            mbti1 = "용감한 수호자(ISFJ)"
            mbti2 = "수호자형 사람은 꽤 독특한 특징을 가지고 있는데, 이 유형에 속하는 사람은 이들을 정의하는 성격 특성에 꼭 들어맞지 않는다는 점입니다. 타인을 향한 연민이나 동정심이 있으면서도 가족이나 친구를 보호해야 할 때는 가차 없는 모습을 보이기도 합니다. 조용하고 내성적인 반면 관계술에 뛰어나 인간관계를 잘 만들어갑니다. 안정적인 삶을 지향하지만 이들이 이해받고 존경받는다고 생각되는 한에서는 변화를 잘 수용합니다. 이처럼 수호자형 사람은 한마디로 정의 내리기 힘든 다양한 성향을 내포하고 있는데, 이는 오히려 그들의 장점을 승화시켜 그들 자신을 더욱 돋보이게 합니다."
            famous = "Halle Berry / Beyonce / Vin Diesel / Kate Middleton"
        elif my_1st_type == "ESTJ":
            mbti1 = "엄격한 관리자(ESTJ)"
            mbti2 = "관리자형 사람은 그들 생각에 반추하여 무엇이 옳고 그른지를 따져 사회나 가족을 하나로 단결시키기 위해 사회적으로 받아들여지는 통념이나 전통 등 필요한 질서를 정립하는 데 이바지하는 대표적인 유형입니다. 정직하고 헌신적이며 위풍당당한 이들은 비록 험난한 가시밭길이라도 조언을 통하여 그들이 옳다고 생각하는 길로 사람들을 인도합니다. 군중을 단결시키는 데에 일가견이 있기도 한 이들은 종종 사회에서 지역사회조직가와 같은 임무를 수행하며, 지역 사회 발전을 위한 축제나 행사에서부터 가족이나 사회를 하나로 결집하기 위한 사회 운동을 펼치는 데 사람들을 모으는 역할을 하기도 합니다."
            famous = "Sonia Sotomayor / Judge Judy / Frank Sinatra / Laura Linney"
        elif my_1st_type == "ESFJ":
            mbti1 = "사교적인 외교관(ESFJ)"
            mbti2 = "사교형 사람을 한마디로 정의 내리기는 어렵지만, 간단히 표현하자면 이들은 '인기쟁이'입니다. 인구의 대략 12%를 차지하는 꽤 보편적인 성격 유형으로, 이를 미루어 보면 왜 이 유형의 사람이 인기가 많은지 이해가 갑니다. 종종 고등학교에서 치어리더나 풋볼의 쿼터백으로 활동하기도 하는 이들은 분위기를 좌지우지하며 여러 사람의 스포트라이트를 받거나 학교에 승리와 명예를 불러오도록 팀을 이끄는 역할을 하기도 합니다. 이들은 또한 훗날 다양한 사교 모임이나 어울림을 통해 주위 사람들에게 끊임없는 관심과 애정을 보임으로써 다른 이들을 행복하고 즐겁게 해주고자 노력합니다."
            famous = "Bill Clinton / Taylor Swift / Jennifer Garner / Steve Harvey"
        elif my_1st_type == "ISTP":
            mbti1 = "만능 재주꾼(ISTP)"
            mbti2 = "냉철한 이성주의적 성향과 왕성한 호기심을 가진 만능재주꾼형 사람은 직접 손으로 만지고 눈으로 보면서 주변 세상을 탐색하는 것을 좋아합니다. 무엇을 만드는 데 타고난 재능을 가진 이들은 하나가 완성되면 또 다른 과제로 옮겨 다니는 등 실생활에 유용하면서도 자질구레한 것들을 취미 삼아 만드는 것을 좋아하는데, 그러면서 새로운 기술을 하나하나 터득해 나갑니다. 종종 기술자나 엔지니어이기도 한 이들에게 있어 소매를 걷어붙이고 작업에 뛰어들어 직접 분해하고 조립할 때보다 세상에 즐거운 일이 또 없을 것입니다. 전보다 조금은 더 향상된 모습으로요."
            famous = "Clint Eastwood / Milla Jovovich / Olivia Wilde / Bear Grylls"
        elif my_1st_type == "ISFP":
            mbti1 = "호기심 많은 예술가(ISFP)"
            mbti2 = "모험가형 사람은 일반적으로 사람들이 생각하듯 야외에서 앙증맞은 나무 그림을 그리고 있는 그런 유형의 예술가는 아니지만, 진정한 예술가라고 할 수 있습니다. 실상 상당수 많은 이들이 그러한 능력을 충분히 갖추고 있기도 합니다. 이들은 그들의 심미안이나 디자인 감각, 심지어는 그들의 선택이나 행위를 통하여 사회적 관습이라는 한계를 뛰어넘고자 합니다. 실험적인 아름다움이나 행위를 통해 전통적으로 기대되는 행동양식이나 관습에 도전장을 내미는 이들은 '저를 가두어두려 하지 마세요!'라고 수없이 외칩니다."
            famous = "Kevin Costner / Avril Lavigne / Michael Jackson / Britney Spears"
        elif my_1st_type == "ESTP":
            mbti1 = "모험을 즐기는 사업가(ESTP)"
            mbti2 = "주변에 지대한 영향을 주는 사업가형 사람은 여러 사람이 모인 행사에서 이 자리 저 자리 휙휙 옮겨 다니는 무리 중에서 어렵지 않게 찾아볼 수 있습니다. 직설적이면서도 친근한 농담으로 주변 사람을 웃게 만드는 이들은 주변의 이목을 끄는 것을 좋아합니다. 만일 관객 중 무대에 올라올 사람을 호명하는 경우, 이들은 제일 먼저 자발적으로 손을 들거나 아니면 쑥스러워하는 친구를 대신하여 망설임 없이 무대에 올라서기도 합니다. 국제사회 이슈나 이와 관련한 복잡하고 난해한 이론과 관련한 담화는 이들의 관심을 오래 붙잡아 두지 못합니다. 사업가형 사람은 넘치는 에너지와 어느 정도의 지식으로 대화에 무리 없이 참여하기는 하나, 이들이 더 역점을 두는 것은 앉아서 말로만 하는 논의가 아닌 직접 나가 몸으로 부딪히는 것입니다."
            famous = "Jack Nicholson / Eddie Murphy / Madonna / Bruce Willis"
        elif my_1st_type == "ESFP":
            mbti1 = "자유로운 영혼의 연예인(ESFP)"
            mbti2 = "갑자기 흥얼거리며 즉흥적으로 춤을 추기 시작하는 누군가가 있다면 이는 연예인형의 사람일 가능성이 큽니다. 이들은 순간의 흥분되는 감정이나 상황에 쉽게 빠져들며, 주위 사람들 역시 그런 느낌을 만끽하기를 원합니다. 다른 이들을 위로하고 용기를 북돋아 주는 데 이들보다 더 많은 시간과 에너지를 소비하는 사람 없을 겁니다. 더욱이나 다른 유형의 사람과는 비교도 안 될 만큼 거부할 수 없는 매력으로 말이죠. 천부적으로 스타성 기질을 타고난 이들은 그들에게 쏟아지는 스포트라이트를 즐기며 어디를 가나 모든 곳이 이들에게는 무대입니다. 사실상 많은 배우가 이 성격 유형에 속하기도 합니다.매우 사교적인 성향의 이들은 단순한 것을 좋아하며, 좋은 사람들과 어울려 즐거운 시간을 갖는 것보다 세상에 더 큰 즐거움은 없다고 여깁니다."
            famous = "Adele / Jamie Oliver / Jamie Foxx / Marilyn Monroe"

        interview_length = len(interview_contents)
        for i in range(interview_length):
            Que.answer_alltext += interview_contents[i]
            i += 1
        mbti2_sum = mbti2 + mbti2 + mbti2 + mbti2
        Que.answer_alltext += mbti2_sum
        print(Que.answer_alltext)

        nlpy = Twitter()
        nouns = nlpy.nouns(Que.answer_alltext)
        print(nouns)

        count = Counter(nouns)
        tag_count = []
        tags = []

        for n, c in count.most_common(1000):
            dics = {'tag': n, 'count': c}
            if len(dics['tag']) >= 2 and len(tags) <= 49:
                tag_count.append(dics)
                tags.append(dics['tag'])

        for tag in tag_count:
            print(" {:<14}".format(tag['tag']), end='\t')
            print("{}".format(tag['count']))

        Que.word = tag
        Que.word_count = tag_count

        print("\n---------------------------------")
        print("     명사 총  {}개".format(len(tags)))
        print("---------------------------------\n\n")

        Que.mbti = my_1st_type
        Que.mbti1 = mbti1
        Que.mbti2 = mbti2
        Que.famous = famous
        Que.save()
        Quet.save()
        del interview_contents[:]

    return JsonResponse(fulfillmentText, safe=True)