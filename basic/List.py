# 리스트명 = [요소1, 요소2, 요소3]
odd = [1, 3, 5, 7, 9]
# 리스트의 인데싱
a = [1, 2, 3]
print(a)
print(a[0] + a[2])
print(a[-1])
a = [1, 2, 3, ['a', 'b', 'c']]
print(a[0])
print(a[-1])
print(a[3])
print(a[-1][0])
print(a[-1][1])
print(a[-1][2])
# 삼중 리스트에서 인데싱하기
a = [1, 2, ['a', 'b', ['Life', 'is']]]
print(a[2][2][0])
# 리스트의 슬라이싱
a = [1, 2, 3, 4, 5]
print(a[0:2])
a = "12345"
print(a[0:2])
a = [1, 2, 3, 4, 5]
b = a[:2]
c = a[2:]
print(b)