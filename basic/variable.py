# 02-8 자료형의 값을 저장하는 공간, 변수
a = 1
b = "python"
c = [1, 2, 3]

print(type(3))

a = 3
b = 3
print(a is b)

# 변수를 만드는 여러 가지 방법
a, b = ('python', 'life')
(a, b) = 'python', 'life'
[a, b] = ['python', 'life']
a = b = 'python'

a = 3
b = 5
a, b = b, a
print(a)
print(b)

# 메모리에 생성된 변수 없애기

a = 3
b = 3
del (a)
del (b)
