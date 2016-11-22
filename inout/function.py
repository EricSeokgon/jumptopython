# 04-1 함수
'''
파이썬 함수의 구조
def 한수명(입력 인수):
    <수행할 문장1>
    <수행할 문장2>
    ...
'''


def sum(a, b):
    return a + b


a = 3
b = 4
c = sum(a, b)
print(c)

# 입력값과 결과값에 따른 함수의 형태

# 일반적인 함수
'''
def 함수이름(입력인수):
    <수행할 문장>
    ...
    return 결과값
'''


def sum(a, b):
    result = a + b
    return result


a = sum(3, 4)
print(a)


# 입력값이 없는 함수
def say():
    return "Hi"


a = say()
print(a)


# 결과값이 없는 함수
def sum(a, b):
    print("%d, %d의 합은 %d입니다." % (a, b, a + b))


sum(3, 4)

a = sum(3, 4)
print(a)


# 입력값도 결과값도 없는 함수
def say():
    print("Hi")


say()

# 입력값이 몇 개가 될지 모를 때는 어떻게 해야 할까?

'''
def 함수이름(*입력변수):
    <수행할 문장>
    ...
'''


# 여러 개의 입력값을 받는 함수 만들기

def sum_many(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum


result = sum_many(1, 2, 3)
print(result)

result = sum_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(result)


def sum_mul(choice, *args):
    if choice == "sum":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result


result = sum_mul('sum', 1, 2, 3, 4, 5)
print(result)
result = sum_mul('mul', 1, 2, 3, 4, 5)
print(result)


# 함수의 결과값은 언제나 하나이다.
def sum_and_mul(a, b):
    return a + b, a * b


result = sum_and_mul(3, 4)

result = (7, 12)

sum, mul = sum_and_mul(3, 4)


def sum_and_mul(a, b):
    return a + b
    return a * b


result = sum_and_mul(2, 3)
print(result)


def sum_and_mul(a, b):
    return a + b


# 입력 인수에 초기값 미리 설정하기
def say_myself(name, old, man=True):
    print("나의 이름은  %s 입니다." % name)
    print("나이는 %d살입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")


say_myself("이석곤", 35)
say_myself("이석곤", 35, False)

#함수 안에서 선언된 변수의 효력 범위
def vartest(hello):
    hello = hello + 1


def vertest(a):
    a = a + 1
vertest(3)
print(a)