# 03-2 while문

# while문의 기본 구조
'''
while <조건문>:
    <수행할 문장1>
    <수행할 문장2>
    <수행할 문장3>
'''
'''
열 번 찍어 안 넘어 가는 나무 없다
'''
treeHit = 0
while treeHit < 10:
    treeHit = treeHit + 1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다.")

# while문 직접 만들기
prompt = """""
    1. add
    2. del
    3. list
    4. quit
    Enter number:"""

number = 0
while number != 4:
    print(prompt)
    number = int(input())

# while문 강제로 빠져나가기

coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee - 1
    print("남은 커피의 양은 %d개입니다." % coffee)
    if not coffee:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break
