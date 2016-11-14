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

'''
prompt = ""
1. add
2. del
3. list
4. quit
Enter number:""

'''
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
