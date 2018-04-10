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
