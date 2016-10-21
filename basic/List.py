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
print(c)
# 중첩된 리스트에서 슬라이싱하기
a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
print(a[2:5])
print(a[3][:2])
# 리스트 연산자
# 1.리스트 더하기(+)
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)
# 2.리스트 반복하기(*)
a = [1, 2, 3]
print(a * 3)
print(str(a[2]) + "hi")
# 리스트의 수정, 변경과 삭제
# 1.리스트에서 하나의 값 수정하기
a = [1, 2, 3]
a[2] = 4
print(a)
# 2.리스트에서 연속된 범위의 값 수정하기
print(a[1:2])
a[1:2] = ['a', 'b', 'c']
print(a)
# 3.[]사용해 리스트 요소 삭제하기
a[1:3] = []
print(a)
# 4.del함수 사용해 리스트 요소 삭제하기
del a[1]
print(a)
# 리스트 관련 함수들
# 리스트에 요소 추가(append)
a = [1, 2, 3]
a.append(4)
print(a)
a.append([5, 6])
print(a)
# 리스트 정렬(sort)
a = [1, 4, 3, 2]
a.sort()
print(a)
a = ['a', 'd', 'c', 'b']
a.sort()
print(a)
# 리스트 뒤집기(reverse)
a = ['a', 'b', 'c']
a.reverse()
print(a)
# 위치 변환(iondex)
a = [1, 2, 3]
print(a.index(3))
print(a.index(1))
# 리스트에 요소 삽입(insert)
a = [1, 2, 3]
a.insert(0, 4)
print(a)
a.insert(3, 5)
print(a)
# 리스트 요소 제거(remove)
a = [1, 2, 3, 1, 2, 3]
a.remove(3)
print(a)
# 리스트 요소 끄집어내기(pop)
a = [1, 2, 3]
a.pop()
print(a)
a = [1, 2, 3]
a.pop(1)
print(a)
# 리스트에 포함된 요소 x의 개수 세기(count)
a = [1, 2, 3, 1]
print(a.count(1))
