"""
    날짜 : 2020/06/23
    이름 : 최정한
    내용 : 함수 입출력 교재 p168
"""

# 입력함수
num = input('숫자 입력 :')

# 출력함수
print('입력한 숫자 :', num)

# 함수정의
def grade(score):
    if 90 <= score <= 100:
        print('A입니다.')

    elif 80 <= score < 90:
        print('B입니다.')

    elif 70 <= score < 80:
        print('C입니다.')

    elif 60 <= score < 70:
        print('D입니다.')

    else:
        print('F입니다.')

# 함수호출
while True:
    # 점수입력
    score = input('점수 입력(종료는 0) : ')

    # 문자열을 숫자로 변환
    sc = int(score)

    if sc == 0 :
        break

    grade(sc)

print('프로그램 종료...')


















