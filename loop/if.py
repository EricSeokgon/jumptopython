money = 1
if money:
    print("택시를 타세요")
else:
    print("버스를 타세요")

'''
if문의 기본 구조

if 조건문:
    수행할 문장1
    수행할 문장2
    ...
else:
    수행할 문장A
    수행할 문장B
    ...
    
    
    if 조건문:
    수행할 문장1
    수행할 문장2
    수행할 문장3
    
    if 조건문:
        수행할 문장1
    수행할 문장2
        수행할 문장3
    
'''

pocket = ['paper', 'cellphone']
card = 1
if 'money' in pocket:
    print("택시를 타세요")
elif card:
    print("택시를 타세요")
else:
    print("버스를 타세요")

print(1 in [1, 2, 3])
print(1 not in [1, 2, 3])

'''
If <조건문>:
    <수행할 문장1> 
    <수행할 문장2>
    ...
elif <조건문>:
    <수행할 문장1>
    <수행할 문장2>
    ...
elif <조건문>:
    <수행할 문장1>
    <수행할 문장2>
    ...
...
else:
   <수행할 문장1>
   <수행할 문장2>
   ... 
'''

a = "Life is too short, you need python"
if 'wife' in a:
    print('wife')
elif 'python' in a and 'you' not in a:
    print('python')
elif 'shirt' not in a:
    print('shirt')
elif 'need' in a:
    print('need')
else:
    print('none')
