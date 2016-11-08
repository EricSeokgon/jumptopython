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
print('a' in ('a', 'b', 'c'))
print('j' not in 'python')

'''
만약 주머니에 돈이 있으면 택시를 타고, 없으면 걸어 가라
'''

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시를 타고가라")
else:
    print("걸어가라")

'''
주머니에 돈이 있으면 가만히 있고, 주머니에 돈이 없으면 카드를 꺼내라
'''

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")

'''
주머니에 돈이 있으면 택시를 타고, 주머니에 돈은 없지만 카드가 있으면 택시를 타고,
돈도 없고 카드도 없으면 걸어 가라
'''

pocket = ['paper', 'handphone']
card = 1
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    if card:
        print("택시를 타고 가라")
    else:
        print("걸어가라")

pocket = ['paper', 'handphone']
card = 1
if 'money' in pocket:
    print("택시를 타고 가라")
elif card:
     print("택시를 타고 가라")
else:
     print("걸어가라")

