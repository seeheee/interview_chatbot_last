# InterviewBot
## Skill Stack
* Language : Python
* FrameWork : Django
* Web : HTML, CSS
* Database : SQLite
* OS : Linux, Windows
* OpenSource : Konlpy, Bootstrap

## Requirement
* Django
* django-crispy-forms
* django-mailgun
* konlpy
* bootstrap

## How to Run
* run saveQuestion.py -> python saveQuestion.py
* runserver -> python manage.py runserver
* If Bot Copy is't run, run ngrok and webhook django with dialogflow

## 💡 Architecture
![image](https://user-images.githubusercontent.com/53335160/125192436-d3aeb480-e282-11eb-8662-c5e7adabdd8e.png)

## 💡 핵심 기능
1. 자기소개서를 분석하여 면접챗봇 진행 후 이에 대한 결과를 그래프와 워드 클라우드로 보여준다.
2. 자기소개서를 여러 개 작성하여 조회/삭제가 가능하다.

## 💡 사용자 피드백 후 바뀐 부분
내용: 자기소개서에서 어떤 기준으로 분석한 것인지 사용자는 믿을 수 없다.
해결방법: MBTI 분석도 하여 객관성 확보
**자기소개서를 MBTI 단어에 맞게 분석하여 그냥 MBTI 검사와 비교해서 일치 불일치 보여준다.**

