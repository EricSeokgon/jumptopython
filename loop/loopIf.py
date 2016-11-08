# 03-1 if문

money = 1
if money:
    print("택시를 타고 간라")
else:
    print("걸어 가라")

# if문의 기본 구조

'''
if 조건문:
    수행할 문장1
    수행할 문장2
    ...
else:
    수행할 문장A
    수행할 문장B
    ...
'''

# 들여쓰기
'''
if 조건문:
    수행할 문장1
    수행할 문장2
    수행할 문장3

if 조건문:
    수행할 문장1
수행할 문장2
    수행할 문장3
'''
'''
if money:
        print("택시를")
    print("타고")
File "<stdin>", line
print("타고")
'''

# 조건문이란 무엇인가?
x = 3
y = 2
print(x > y)
print(x < y)
print(x == y)
print(x != y)
'''
만약 3000원 이상의 돈으 ㄹ가지고 있으면 택시를 타고 그렇지 않으면 걸어 가라
'''
money = 2000
if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어가라")

'''
돈이 3000원 이상 있거나 카드가 있다면 택시를 타고 그렇지 않으면 걸어 가라
'''

money = 2000
card = 1
if money > 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어가라")

print(1 in [1, 2, 3])
print(1 not in [1, 2, 3])
