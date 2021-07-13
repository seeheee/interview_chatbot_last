# 자기소개서 기반 인공지능 챗봇 미리매


### 💎 시연 동영상 다운로드 💎
[한이음공모전_인공지능챗봇_미리매_동영상.zip](https://github.com/seeheee/interview_chatbot_last/files/6799342/_._._.zip)


### 💡 Architecture
![image](https://user-images.githubusercontent.com/53335160/125192436-d3aeb480-e282-11eb-8662-c5e7adabdd8e.png)


### 💡 핵심 기능
1. 자기소개서를 분석하여 이를 기반으로 한 질문의 면접챗봇 진행하여 각각 개인의 특성에 맞게 연습해보도록 한다.
2. 면접 결과에 대한 답변을 자신이 각각 점수를 줄 수 있다.
3. 자기소개서 분석 결과를 2가지의 그래프와 워드 클라우드로 그 결과를 보여준다.
4. 자기소개서를 여러 개 작성하여 조회/삭제가 가능하다.
5. 자기소개서로 분석한 MBTI와 설문을 통한 MBTI를 비교하여 자기소개서와 면접의 일치성을 부여한다.


### 💡 사용자 피드백 후 바뀐 부분
1️⃣ 내용: 자기소개서에서 어떤 기준으로 분석한 것인지 사용자는 믿을 수 없다.<br>
1️⃣ 해결방법: MBTI 분석도 하여 객관성 확보, 자기소개서를 MBTI 단어에 맞게 분석하여 그냥 MBTI 검사와 비교해서 일치 불일치 보여준다.<br>

2️⃣ 내용: 마이페이지에서 보여주는 결과가 부족하다. 더 많은 정보가 있었음 좋겠다.<br>
2️⃣ 해결방법: 워드 클라우드와 마름모 그래프 추가<br>

### 💡 아쉬운 점
Google Assistant API의 연결은 성공했지만 음성을 DB에 저장하여 이를 다시 분석하여 면접 결과에 대한 피드백을 주는 것을 하지 못했다...

### 💡 Requirement Pakage
* django-crispy-forms - 장고 폼을 부트스트랩 버전으로 바꿔줌
* django-mailgun - 장고 이메일 백엔드
* konlpy - 한국어 형태소 분석

### How to Run
* run saveQuestion.py -> python saveQuestion.py
* runserver -> python manage.py runserver
* If Bot Copy is't run, run ngrok and webhook django with dialogflow

python manage.py startapp "이름"<br>
![image](https://user-images.githubusercontent.com/53335160/125417840-1972d645-3d61-49b0-9a72-a9973ccb1f87.png)

## 💡 형태소 분석 KoNLPy 패키지 Twitter
https://hyrama.com/?p=463<br>
https://konlpy-ko.readthedocs.io/ko/v0.4.3/api/konlpy.tag/


