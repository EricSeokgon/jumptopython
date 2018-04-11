# 02-2 문자열 자료형
# 1.큰따옴표로 양쪽 둘러싸기
print("Hello World")

# 2.작은 따옴표로 양쪽 둘러싸기
print('Python is fun')

# 3.큰따옴표 3개를 연속으로 써서 양쪽 둘러싸기
print("""Hello World""")

# 4.작은따옴표 3개를 연속으로 써서 양쪽 둘러싸기
print('''Hello World''')

# 문자열에 작은따옴표 ' 포함시키기
food = "Python's favorite food is perl"
print(food)

# 문자열에 큰땅모표 " 포함시키기

say = '"Python is very easy." he says.'
print(say)

# \(백슬래시)를 이용해서 작은 따옴표 ' 와 큰따옴표"를 문자열에 포함시키기

food = 'Python\'s favorite food is perl'
say = "\"Python is very easy.\" he says."
print(food)
print(say)

# 여러 줄인 문자열을 변수에 대입하고 싶을 때
multiline = '''
Life is too short
You need python
'''
print(multiline)
multiline = """
Life is too short
You need python
"""
print(multiline)

# 문자열 연산하기
# 1)문자열 더해서 연결하기
head = "Python"
tail = "is fun!"
print(head + tail)

# 2)문자열 곱하기
a = "python"
print(a * 2)

# 3)문자열 곱하기 응용

print("=" * 50)
print("My Program")
print("=" * 50)

# 문자열 인데싱과 슬라이싱
# 문자열 인덱싱이란?
a = "Life is too short, you need Python"
print(a[3])

# 문자열 인덱싱 활용하기
a = "Life is too short, you need Python"
print(a[0])
print(a[12])
print(a[-1])

# 문자열 슬라이싱이란?
a = "Life is too short, you need Python"
b = a[0] + a[1] + a[2] + a[3]
print(b)

a = "Life is too short, you need Python"
print(a[0:4])

# 문자열을 슬라이싱하는 방법
a = "Life is too short, you need Python"
print(a[0:5])
print(a[0:2])
print(a[5:7])
print(a[12:17])

# 슬라이싱으로 문자열 나누기
a = "20010331Rainy"
date = a[:8]
weather = a[8:]
print(date)
print(weather)

# "Pithon"이라는 문자열을 "Python"으로 바꾸려면?
a = "Pithon"
print(a[:1] + 'y' + a[2:])

# 문자열 포매팅 따라하기
# 1)숫자 바로 대입
print("I eat %d apples." % 3)

# 2)문자열 바로 대입
print("I eat %s apples." % "five")

# 3)숫자 값을 나타내는 변수로 대입
number = 3
print("I eat %d apples." % number)
