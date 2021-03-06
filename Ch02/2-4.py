"""
    날짜 : 2020/06/22
    이름 : 최정한
    내용 : 튜플 자료형 실습하기 교재 p85
"""

# 튜플 생성하기
tp1 = (1, 2, 3, 4, 5)
tp2 = 1, 2, 3, 4, 5
tp3 = '김유신', '김춘추', '장보고', '강감찬', '이순신'

# 튜플 원소 출력
print('tp1 : ', tp1)
print('tp2 : ', tp2)
print('tp2[1] : ', tp2[1])
print('tp2[2] : ', tp2[4])
print('tp3[0] : ', tp3[0])
print('tp3[4] : ', tp3[4])

# 튜플 원소 삭제 - 튜플은 정적 리스트이므로 원소 삭제를 할 수 없음
# del tp1[0]

# 튜플 원소 수정 - 튜플은 정적 리스트이므로 원소 수정을 할 수 없음
# tp2[0] = 7

# 교재 p86 ~ 87 실습하기
# 튜플의 원소 삭제, 수정 안됨

# 인덱싱
t1 = (1, 2, 'a', 'b')
print('t1 :', t1[0])
print('t1 :', t1[3])

# 슬라이싱
t1 = (1, 2, 'a', 'b')
print('t1 :', t1[1:]) # t1[1:] <- t1[1]부터 끝까지

# 튜플 더하기
t1 = (1, 2, 'a', 'b')
t2 = (3, 4)

print('t3 :', t1 + t2)

# 튜플 곱하기
print('t3 : ', t2*3)

# 튜플 길이 구하기
t1 = (1, 2, 'a', 'b')
print('t1 : ', len(t1))

