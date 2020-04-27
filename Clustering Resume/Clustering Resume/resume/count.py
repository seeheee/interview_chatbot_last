from konlpy.tag import Twitter
from collections import Counter
from .models import Propensity

def get_tags(text, ntags=50):
    spliter = Twitter()
    # konlpy의 Twitter객체
    nouns = spliter.nouns(text)
    # nouns 함수를 통해서 text에서 명사만 분리/추출
    count = Counter(nouns)
    # Counter객체를 생성하고 참조변수 nouns할당
    return_list = []  # 명사 빈도수 저장할 변수
    for n, c in count.most_common(ntags):
        temp = {'tag': n, 'count': c}
        return_list.append(temp)
    # most_common 메소드는 정수를 입력받아 객체 안의 명사중 빈도수
    # 큰 명사부터 순서대로 입력받은 정수 갯수만큼 저장되어있는 객체 반환
    # 명사와 사용된 갯수를 return_list에 저장합니다.
    return return_list


def run_count(input):
    # # 분석할 파일
    # noun_count = 200
    # # 최대 많은 빈도수 부터 20개 명사 추출
    # output_file_name = "motive_cnt.txt"
    # # count.txt 에 저장
    #
    # # 분석할 파일을 open
    # text = input  # 파일을 읽습니다.
    # tags = get_tags(text, noun_count)  # get_tags 함수 실행
    # open_output_file = open(output_file_name, 'w', -1)
    # # 결과로 쓰일 count.txt 열기
    # for tag in tags:
    #     noun = tag['tag']
    #     count = tag['count']
    #     if len(noun) == 1:
    #         continue
    #     open_output_file.write('{} {}\n'.format(noun, count))
    # # 결과 저장
    # open_output_file.close()
    # f = open("resume3.txt", 'r')
    # token = f.read()
    token = input
    # token=re.sub("(\.)","","정부가 발표하는 물가상승률과 소비자가 느끼는 물가상승률은 다르다.")
    # 정규 표현식을 통해 온점을 제거하는 정제 작업입니다.
    spliter = Twitter()
    token = spliter.nouns(token)
    # OKT 형태소 분석기를 통해 토큰화 작업을 수행한 뒤에, token에다가 넣습니다.

    a = {'스스로', '적극', '도전', '준비', '관심', '참여', '직접', '능력', '의견', '열정', '최선', '최고', '역량'}
    b = {'긍정', '경험', '활동', '프로그램', '팀원', '근무'}
    c = {'노력', '시간', '준비', '정보', '구현', '지식', '공부', '편입', '항상', '성장', '개발'}
    d = {'책임감', '관리', '해결', '역할', '팀원', '의견', '성과'}
    e = {'친구', '관계', '사랑', '배려', '도움'}
    f = {'집중', '계획', '목표', '신뢰', '시간', '과정', '결과', '기획', '준비', '설계'}
    # 13,6,11,7,5,10

    bow = [0, 0, 0, 0, 0, 0]

    for voca in token:
        if voca in a:
            bow[0] = bow[0] + 1
        elif voca in b:
            bow[1] = bow[1] + 1
        elif voca in c:
            bow[2] = bow[2] + 1
        elif voca in d:
            bow[3] = bow[3] + 1
        elif voca in e:
            bow[4] = bow[4] + 1
        elif voca in f:
            bow[5] = bow[5] + 1

    bow[0] = bow[0] / 13
    bow[1] = bow[1] / 6
    bow[2] = bow[2] / 11
    bow[3] = bow[3] / 7
    bow[4] = bow[4] / 5
    bow[5] = bow[5] / 10

    result = 0

    for a in range(6):
        result = result + bow[a]

    for a in range(6):
        bow[a] = round((bow[a] / result) * 100, 1)

    Pro = Propensity()

    Pro.score1 = bow[0]
    Pro.score2 = bow[1]
    Pro.score3 = bow[2]
    Pro.score4 = bow[3]
    Pro.score5 = bow[4]
    Pro.score6 = bow[5]

    Pro.save()
    print(bow)

