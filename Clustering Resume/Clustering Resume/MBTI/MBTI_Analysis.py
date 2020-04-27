from konlpy.tag import Twitter
from collections import Counter
import os
import operator

def main():
    dic = {'E': ['책임감', '관리', '해결', '팀원', '열정', '역량', '참여', '직접', '활동', '정열', '외부', '사람', '행동', '모임', '공동체', '공적', '말', '도시', '토론', '외향성', '대인관계', '유지', '사교', '자기', '집중', '적극성', '말로', '경험', '다음', '이해', '스스로','적극', '도전',],
           'I': ['생각', '이해', '경험', '집중', '장소', '도서관', '개인', '사적', '숲', '내향성', '깊이', '대인관계', '유지', '자기', '내부', '부활동', '신중', '글', '서서히'],
           'S': ['실제', '나무', '사실', '감각', '경험', '지금', '현재', '초점', '정확', '처리', '관찰', '생산', '보존', '거북이', '오감', '의존', '중시', '사건', '묘사', '경향', '추수', '함'],
           'N': ['가능성', '숲', '미래', '신속', '처리', '상상력', '이론', '디자인', '통찰', '변화', '토끼', '직관', '육감', '영감', '의존', '지향', '의미', '추구', '초점', '아이디어', '비유', '암시', '묘사', '경향'],
           'T': ['진실', '논리', '분석', '사실', '관심', '정의', '머리', '관성', '질서', '공평', '사고', '객관', '판단', '원리', '원칙', '규범', '기준', '중시', '지적', '논평', '신뢰'],
           'F': ['팀원', '긍정', '관계', '관심', '상황', '의미', '자비', '가슴', '열정', '재치', '조화', '가치', '친절', '중심', '감정', '사람과', '정상', '참작', '설명', '사람', '영향', '포괄', '나', '우호', '협조', '친구', '배려', '도움', '사랑'],
           'J': ['개발', '프로젝트', '기획', '준비', '설계', '계획', '조직', '방향', '과단성', '집중', '일', '지배인', '결과', '판단', '목적', '목표', '기한', '엄수', '사전', '체계', '정리', '정돈', '의지', '추진', '결론', '통제', '조정', '목적의식', '감각', '기준', '자기', '의사', '신뢰'],
           'P': ['의견', '융통', '과정', '목적', '방향', '변화', '상황', '개방', '자유', '호기심', '즉흥', '질문', '놀이', '기업가', '시작', '인식', '일정', '자율', '융통성', '이해', '수용', '적응', '재량', '처리']}

    dic_sum ={  'ENFJ': ['사람', '생각', '의견', '외교', '충성', '경향', '적극', '책임감', '사교성', '사교', '참을성', '관심', '동선', '대체로', '동의', '현재', '미래', '가능성', '추구', '능란', '계획', '제시', '집단', '능력', '교직', '성직', '심리', '상담', '치료', '예술', '문학', '판매', '맹목', '대해', '자기', '이상', '개인', '언어', '표현', '성적', '열정', '염려', '지적', '마음'],
                'ENFP': ['일', '열성', '재능', '창의', '관심', '사람', '통찰', '정열', '활기', '상상력', '정적', '항상', '가능성', '시도', '문제해결', '수행', '능력', '도움', '상담', '교육', '과학', '저널리스트', '광고', '판매', '성직', '작가', '분야', '반복', '일상', '창의력', '요구', '흥미', '호기심', '성적', '재주', '자발', '표현', '독립', '우호', '열정', '상상', '활동'],
                'ENTJ': ['계획', '감정', '통솔력', '결정', '관심', '논리', '필요', '자신', '열성', '단호', '지도력', '활동', '장기', '안목', '선호', '지식', '욕구', '지적', '자극', '아이디어', '처리', '준비', '분석', '조직', '체계', '추진', '의견', '귀', '타인', '느낌', '인정', '판단', '결론', '피해', '누적', '크게', '폭발', '가능성', '전략', '비판', '조절', '도전', '직선', '객관', '이론'],
                'ENTP': ['일', '문제', '능력', '독창', '안목', '다방면', '관심', '재능', '도전', '분석', '이론', '창의력', '상상력', '시도', '솔선', '논리', '해결', '사람', '동향', '대해', '일상', '세부', '경시', '즉', '흥미', '수행', '가지', '발명가', '과학자', '해결사', '저널리스트', '마케팅', '컴퓨터', '등', '때', '경쟁', '현실', '더', '편이', '진취', '독립', '전략', '창의', '융통성', '자원'],
                'ESFJ': ['사람', '이야기', '요구', '마음', '양심', '관심', '협력', '동료', '능동', '구성원', '정리정돈', '참을성', '행동', '교직', '성직', '판매', '필요', '간호', '의료', '일이', '대한', '문제', '입장', '반대', '의견', '자신', '거절', '상처', '충성', '사교', '개인', '협동', '재치', '감동', '전통', '동정'],
                'ESFP': ['사교', '수용', '낙천', '실제', '사람', '일', '상식', '분야', '활동', '현실', '상황', '주위', '관심', '사물', '사실', '물질', '소유', '운동', '실생활', '능력', '필요', '의료', '판매', '교통', '유흥', '간호', '비서', '사무직', '감독', '기계', '수다', '깊이', '마무리', '경향', '조직체', '공동체', '분위기', '조성', '역할', '성적', '융통성', '우호', '표현', '협동', '관용', '개방'],
                'ESTJ': ['현실', '조직', '일', '능력', '분야', '사실', '지도력', '행정', '체계', '결정', '경향', '구체', '활동', '실질', '감각', '계획', '추진', '기계', '재능', '업체', '조직체', '지도자', '목표', '설정', '지시', '이행', '결과', '사업가', '관리', '생산', '건축', '발휘', '속단', '속결', '업무', '사람', '인간', '중심', '가치', '타인', '감정', '고려', '미래', '가능성', '현재', '추구', '실용', '논리', '효율', '객관', '실제', '구조', '인적'],
                'ESTP': ['현실', '사실', '개방', '일', '별로', '문제해결', '적응력', '관용', '사람', '선입관', '감각', '협책', '모색', '문제', '해결', '능력', '적응', '친구', '설명', '운동', '음식', '활동', '주로', '보고', '생활', '순발력', '기억', '예술', '멋', '판단력', '연장', '재료', '논리', '분석', '처리', '추상', '아이디어', '개념', '대해', '흥미', '행동', '지향', '융통성', '재미', '재주', '열정', '낙천', '자발', '실용', '설득'],
                'INFJ': ['분야', '직관', '통찰', '열정', '인내심', '양심', '화합', '추구', '창의력', '말', '타인', '영향력', '독창', '성과', '내적', '독립심', '신념', '자신', '영감', '구현', '정신', '지도자', '사람', '중심', '가치', '중시', '성직', '심리학', '심리치료', '상담', '예술', '문학', '테크니컬', '순수과학', '연구', '개발', '시도', '대한', '열성', '경향', '목적', '달성', '주변', '조건', '경시', '갈등', '내적인', '생활', '소유', '내면', '반응', '남', '공유', '헌신', '창의', '깊이', '결심', '개념', '전체', '이상'],
                'INFP': ['자신', '경향', '정열', '신념', '이상', '일', '인간', '능력', '헌신', '목적', '낭만', '내적', '마음', '관계', '일이', '사람', '책임감', '지향', '남', '지배', '인상', '거의', '완벽', '주의', '노동', '대가', '흥미', '자하', '이해', '복지', '기여', '언어', '문학', '상담', '심리학', '과학', '예술', '분야', '발휘', '현실', '실제', '상황', '고려', '융통성', '모험심', '창의', '깊이', '과묵', '공감'],
                'INTJ': ['독창', '타인', '사고', '비판', '분석', '직관', '자신', '목적', '능력', '노력', '분야', '창의력', '내적', '신념', '행동', '영감', '실현', '의지', '결단', '인내심', '중요시', '달성', '시간', '일', '통찰', '활용', '과학', '엔지니어링', '발명', '정치', '철학', '발휘', '일과', '사람', '그대로', '사실', '감정', '고려', '관점', '독립', '논리', '체계', '마음', '전이', '이론', '기준', '객관', '전체'],
                'INTP': ['논리', '지적', '과묵', '분석', '관심', '호기심', '추상', '문제', '해결', '하나', '대해', '말', '이해', '직관', '통찰', '재능', '개인', '인관', '관계', '친목', '잡담', '객관', '비평', '발휘', '순수과학', '연구', '수학', '엔지니어링', '개념', '경제', '철학', '심리학', '학문', '비현실적', '사교성', '결여', '경향', '자신', '능력', '은근', '과시', '때문', '회의', '초연', '이론', '독립', '사색', '독창', '자율', '자기', '결정'],
                'ISFJ': ['헌신', '자신', '타인', '책임감', '처리', '조직', '정적', '인내력', '다른', '사람', '사정', '고려', '감정', '현실', '감각', '실제', '경험', '통해', '인정', '난관', '밀고', '의존', '독창', '요구', '표현', '관심', '관찰', '분야', '의료', '간호', '교직', '사무직', '사회사업', '일', '대처', '행동', '분별', '상세', '전통', '참을성', '봉사', '보호', '매우', '동정'],
                'ISFP': ['말', '적응력', '관용', '자신', '의견', '타인', '융통성', '연기력', '속마음', '상대방', '동정', '자기', '능력', '성격', '유형', '가장', '가치', '강요', '충돌', '피하', '중시', '인간', '관계', '일', '감정', '결정', '추진', '일상', '활동', '개방', '협동', '충성', '신뢰', '자발', '이해'],
                'ISTJ': ['조직', '집중', '분별', '실제', '사실', '체계', '일', '발휘', '기억', '처리', '책임감', '현실', '감각', '보수', '경향', '문제', '해결', '과거', '경험', '적용', '반복', '일상', '대한', '인내력', '자신', '타인', '감정', '기분', '배려', '전체', '타협', '방안', '고려', '노력', '정확성', '선호', '회계', '법률', '생산', '건축', '의료', '사무직', '관리직', '능력', '위기', '상황', '안정', '신뢰', '확고', '부동', '의무'],
                'ISTP': ['상황', '능력', '객관', '사실', '인생', '관찰', '파악', '도구', '형', '이상', '발휘', '조직', '기계', '과묵', '절제', '호기심', '민감', '성과', '말', '필요', '자신', '일과', '관계', '인간관계', '직접', '가을', '에너지', '소비', '사람', '자료', '정리', '인과관계', '원리', '관심', '연장', '재능', '법률', '경제', '마케팅', '판매', '통계', '분야', '느낌', '감정', '타인', '대한', '마음', '표현', '편의', '실제', '실적', '응용', '독립', '모험', '융통성', '자기', '결정']}

    bow = {'E': 0, 'I': 0, 'S': 0, 'N': 0, 'T': 0, 'F': 0, 'J': 0, 'P': 0}
    bow_sum = {'E': 0, 'I': 0, 'S': 0, 'N': 0, 'T': 0, 'F': 0, 'J': 0, 'P': 0}
# ########################################################################################################################
# 1. 읽어 온 resume을 분석해 mbti 값과 mbti 값에서 유도된 성향점수 반영 후 저장
# 2. resume DB 에 mbti DATA 저장할 수 있도록 DB 수정 후 MBTI DATA 반영
# ########################################################################################################################
    filename = "resume"

    text_file_name = filename + ".txt"

    open_text_file = open(text_file_name, 'rt', encoding='UTF8')
    text = open_text_file.read()  # 파일을 읽습니다.
########################################################################################################################
    spliter = Twitter()
    token = spliter.nouns(text)

    for key in dic.keys():
        for voca in token:
            if voca in dic[key]:
                bow[key] += 1
        bow[key] = bow[key]/len(dic[key])

    for key in dic_sum.keys():
        for voca in token:
            if voca in dic_sum[key]:
                for i in range(0, 4):
                    bow_sum[key[i:i+1]] += 1
        for i in range(0, 4):
            bow_sum[key[i:i+1]] = bow_sum[key[i:i+1]]/len(dic_sum[key])


    mbti_sum = {'E': 0, 'I': 0, 'S': 0, 'N': 0, 'T': 0, 'F': 0, 'J': 0, 'P': 0}

    for key in mbti_sum.keys():
        mbti_sum[key] = bow[key] + bow_sum[key]

    mbti_type = list(mbti_sum.keys())
    mbti_reverse_type = {'E': 'I', 'S': 'N', 'T': 'F', 'J': 'P',
                         'I': 'E', 'N': 'S', 'F': 'T', 'P': 'J'}
    mbti_type_loc = {'E': 0, 'S': 1, 'T': 2, 'J': 3,
                     'I': 0, 'N': 1, 'F': 2, 'P': 3}

    mbti_best_type = {}
    mbti_worst_type = {}

    for i in range(0, 4):
        key = mbti_type[2*i] if mbti_sum[mbti_type[2*i]] > mbti_sum[mbti_type[2*i + 1]] else mbti_type[2*i + 1]
        tmp = {key: abs(mbti_sum[mbti_type[2*i]] - mbti_sum[mbti_type[2*i + 1]])}
        # print(tmp)
        mbti_best_type.update(tmp)
        tmp.clear()

        tmp = {mbti_reverse_type[key]: abs(mbti_sum[mbti_type[2*i]] - mbti_sum[mbti_type[2*i + 1]])}
        # print(tmp)
        mbti_worst_type.update(tmp)
        tmp.clear()
    print("Score Of MBTI and Resume")
    print(bow)
    print("\nScore Of Only MBTI")
    print(bow_sum)
    print("\nSum Of Every Score")
    print(mbti_sum)
    print("\nDifference of Conflicted MBTI Score")
    print(mbti_best_type)
    print(mbti_worst_type)
    print("")

    my_org_type = list(mbti_best_type.keys())
    my_worst_type = "".join(list(mbti_worst_type.keys()))
    print("my_org_type :" + "".join(my_org_type) + "\n")

    my_type_sorted = sorted(mbti_best_type.items(), key=operator.itemgetter(1))
    print("In Order by Difference of Conflicted MBTI Score")
    print(my_type_sorted)
    print("")
    print("The Most Similar Type : " + my_type_sorted[0][0] + "\nThe Second Similar Type : " + my_type_sorted[1][0])
    print("")

    my_1st_type = "".join(my_org_type)

    my_org_type[mbti_type_loc[my_type_sorted[0][0]]] = mbti_reverse_type[my_type_sorted[0][0]]
    my_2nd_type = "".join(my_org_type)
    my_org_type[mbti_type_loc[my_type_sorted[0][0]]] = mbti_reverse_type[my_org_type[mbti_type_loc[my_type_sorted[0][0]]]]

    my_org_type[mbti_type_loc[my_type_sorted[1][0]]] = mbti_reverse_type[my_type_sorted[1][0]]
    my_3rd_type = "".join(my_org_type)

    print("my_1st_type :" + my_1st_type)
    print("my_2nd_type :" + my_2nd_type)
    print("my_3rd_type :" + my_3rd_type + "\n")
    print("my_worst_type : " + my_worst_type)

if __name__ == '__main__':
    main()