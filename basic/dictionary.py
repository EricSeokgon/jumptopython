# 딕셔너리 쌍 추가하기
a = {1: 'a'}
a[2] = 'b'
print(a)
a['name'] = 'pey'
print(a)
a[3] = [1, 2, 3]
print(a)
# 딕셔너리 요소 삭제하기
del a[1]
print(a)
# 딕셔너리를 사용하는 방법
# 딕셔너리에서 key사용해 Value얻기
grade = {'pey': 10, 'julliet': 99}
print(grade['pey'])
print(grade['julliet'])
a = {1: 'a', 2: 'b'}
print(a[1])
print(a[2])
dic = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print(dic['name'])
print(dic['phone'])
print(dic['birth'])

# 딕셔너리 관련 함수들
# Key 리스트 만들기(Keys)
a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print(a.keys())

for k in a.keys():
    print(k)
print(list(a.keys()))

# Value 리스트 만들기 (values)
print(a.values())

# Key:Value 쌍 모두 지우기( clear)
print(a.clear())
