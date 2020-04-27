from konlpy.tag import Twitter
from collections import Counter
import glob
import os #디렉토리를 바꿔야 할 경우에만 쓰세요


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


def main():
    filenames = []
    for file in os.listdir("./"):
        if file.endswith(".txt"):  # 끝이 ".txt"로 끝나는 경우
            filenames.append(file[:-4])
    print(filenames)

    output_file_name = "dic_resume_cnt.txt"
    open_output_file = open("./sum_count/" + output_file_name, 'w', -1)
    open_output_file.write("{ ")
    dirname = "./"
    for filename in filenames:
        text_file_name = filename + ".txt"
        # 분석할 파일
        noun_count = 1000
        # 최대 많은 빈도수 부터 20개 명사 추출
        # count.txt 에 저장
        open_text_file = open(dirname + text_file_name, 'rt', encoding='UTF8')

        # 분석할 파일을 open
        text = open_text_file.read()  # 파일을 읽습니다.
        tags = get_tags(text, noun_count)  # get_tags 함수 실행
        open_text_file.close()  # 파일 close
        # 결과로 쓰일 count.txt 열기
        open_output_file.write("'"+filename + "': "+"['")
        # cnt = 0
        # for tag in tags:
        #     noun = tag['tag']
        #     # count = tag['count']
        #     # if len(noun) == 1:
        #     #     continue
        #     cnt += 1
        #     if cnt == len(tags):
        #         open_output_file.write('{}'.format(noun)+ "'")
        #     else:
        #         open_output_file.write('{}'.format(noun) + "', '")
        open_output_file.write("],\n")
        # 결과 저장
    open_output_file.close()


if __name__ == '__main__':
    main()