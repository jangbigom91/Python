"""
    날짜 : 2020/06/22
    이름 : 최정한
    내용 : 문자열 자료형 실습하기 교재 p44
"""

# 문자열 더하기
str1 = 'Hello\t'
str2 = 'Python!'
str3 = str1 + str2
print('str3 : ', str3)

# 문자열 곱하기
str = 'python!'
print('str * 5 : ', str * 5)

# 문자열 길이
hello = 'Hello World'
print('hello 길이 : ', len(hello))

# 문자열 인덱스
print('hello[0] : ', hello[0])
print('hello[6] : ', hello[6])

# 문자열 슬라이스
print('hello[0:7] : ', hello[0:7])
print('hello[1:7] : ', hello[1:7])
print('hello[:7] : ', hello[:7])
print('hello[7:] : ', hello[7:])
print('hello[-1] : ', hello[-1])
print('hello[-2] : ', hello[-2])

# 문자열 분리
animal = '사자,호랑이,코끼리,기린'
a1, a2, a3, a4 = animal.split(',')

print('a1 :', a1)
print('a2 :', a2)
print('a3 :', a3)
print('a4 :', a4)

# 문자열 포맷
fm1 = '오늘은 %d월 입니다.'
fm2 = '오늘은 %d월 %d일 입니다.'
fm3 = '오늘은 %s월 입니다.'
fm4 = '오늘은 %s년 %d월 %d일 %s요일 입니다.'

print(fm1 % 6)
print(fm2 % (6, 22))
print(fm3 % '06')
print(fm4 % ('2020', 6, 22, '월'))

# 문자열 관련 함수 교재 p67 ~ p71

# 문자 개수 세기(count)
a = "hobby"
a.count('b')
print('a :', a.count('b'))

# 위치 알려주기1(find)
a = "Python is the best choice"
a.find('b')
a.find('k')

print('a :', a.find('b'))
print('a :', a.find('k'))

# 위치 알려주기2(index)
a = "Life is too short"
a.index('t')
#a.index('k') # k가 없기 때문에 오류 발생

print('a :', a.index('t'))
#print('a :', a.index('k')) # k가 없기 때문에 오류 발생

# 문자열 삽입(join)
",".join('abcd')
",".join(['a', 'b', 'c', 'd'])

print('a :', 'a,b,c,d')

# 소문자를 대문자로 바꾸기(upper)
a = "hi"
a.upper()

print('a :', a.upper())

# 대문자를 소문자로 바꾸기(lower)
a = "HI"
a.lower()

print('a :', a.lower())

# 왼쪽 공백 지우기(lstrip)
a = " hi "
print('a :', a.lstrip())

# 오른쪽 공백 주기우기(rstrip)
a = " hi "
print('a :', a.rstrip())

# 양쪽 공백 지우기(strip)
a = " hi "
print('a :', a.strip())

# 문자열 바꾸기(replace)
a = "Life is too short"
print('a :', a.replace("Life", "Your leg"))

# 문자열 나누기(split)
a = "Life is too short"
a.split()
print('a :', a)
