
"""
icecream = {'Tankboy': [1200,5], 'Ppangppare': [1800,2], 'Worldcorn': [1500,4], 'Melona': [1000,1]}

for item in icecream:
    print("{:>6}".format(item), end=' ')
    print("{:3d}개".format(icecream[item][0]), end=' ')
    print("{:10d}원".format(icecream[item][1]))
#print("\n총 구매 소요 비용 %d" % total)

"""
"""
nums = [-1, 10, 2, 8, 9, 7, -11, 20, 21, 37, 56, 21, -27]

print('{}'.format(nums))

sort_nums = []

sort_nums = sorted(nums)

print(sort_nums)


print(sort_nums[:3])
print('smallest:',sort_nums[-3:])
      
"""
# Dictionary 처리

x = {'a': 10, 'c': 30, 'b': 20,  'd': 40}

for key, value in x.items():
     print(key, value)

for key in x.keys():
#     print(key, end=' ')
     print('{:>4}'.format(key))

for value in x.values():
#     print(value, end=' ')
     print('{:4d}'.format(value))

# 평균구하기

avg = 0

avg = sum(x.values()) / len(x)

print( '\n Average  {:3.2f}'.format(avg))


"""
def sum(a, b) :
    return a + b

var = [10, 11]

print(sum(*var))
"""
      
"""
result = 0

result = sum(var[0], var[1])
print(result)
"""


"""

files = ['a.txt', 'b.txt', 'exer.avi', 'sing.mp3', 'ultra.avi']

a = []

for f in files :
    if f.endswith('txt'):
        a.append(f)

#    f = f.split('.')
#    if f[1] =='txt' :
#        a.append(f[0]+'.'+f[1] )

print(a)

"""    


"""

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evenlist = []
oddlist = []

for x in nums :
    if x%2 == 0 :
        evenlist.append(x)
    else :
        oddlist.append(x)

print( "even :", evenlist)
print( "odd :", oddlist)
"""


"""
nums = [1, 2, 3, 4, 5]
rlist = []

for i in nums :
    result = i*i
    rlist.append(result)

print(rlist)
"""    


"""
#dictionary update
contact1 = {'chusu': '010-3111-2393', 'minsu':'010-3112-9932'}
contact2 = {'jaein': '011-1312-2121', 'jongho':'010-8821-1311'}

#contact1.update(contact2)
#contact = contact1

#for name, address in contact.items() :
#    print(name,address)

d = {}

for k, v in contact1.items() :
    d.update({k:v})
for k, v in contact2.items() :
    d.update({k:v})

for k,v in d.items():
    print(k,v)

"""

"""
# Dictionary Min Value
icecream = {'Tankboy': 1200, 'Ppangppare': 1800, 'Worldcorn': 1500, 'Melona': 1000}

for name, price in icecream.items() :
    if price == min(icecream.values()) :
        print (name,price)
"""




# List Index
# 리스트[시작인덱스:끝인덱스]
# 리스트1 + 리스트2 -> 리스트를 서로 연결하며 extend와 동일
# a = [38, 21, 53, 62, 19]
# for index, value in enumerate(a):
#     print(index, value)

# a = [i for i in range(10)]        # 0부터 9까지 숫자를 생성하여 리스트 생성
# a
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# b = list(i for i in range(10))    # 0부터 9까지 숫자를 생성하여 리스트 생성
# b = [i + 5 for i in range(10) if i % 2 == 1]    # 0~9 숫자 중 홀수에 5를 더하여 리스트 생성
# b
# [6, 8, 10, 12, 14]


"""
import math as m

x = 1.5

# ceil : 반올림, floor : 버림
print(m.ceil(x), m.floor(x))

"""

"""
# map 함수
# a, b = map(int,input("두 숫자 입력 ").split())

a = list(map(int,[1.1,2.3]))
a = list(map(str,range(10)))

print(a)
#print(b)
#print(a+b)

"""

######################################################################
#모듈  : 특정 기능을 .py 파일 단위로 작성한 것입니다.
#       ex) import math
#           math.pi
#           import math as m
#           m.pi
#패키지: 특정 기능과 관련된 여러 모듈을 묶은 것입니다.
#        보통 인터넷에 있는 패키지를 설치해서 사용합니다.
#        import 패키지.모듈 as 새이름
#  import urllib.request as r
#   urllib 패키지의 request 모듈을 가져오면서 r로 새 이름 지정
#라이브러리: 파이썬에 기본적으로 설치된 모듈과 내장 함수를 묶어서
#            파이썬 표준 라이브러리(Python Standard Library, PSL)라 부릅니다.


#from 모듈 import 변수
#from 모듈 import 함수
#from 모듈 import 클래스
#from math import sqrt    # math 모듈에서 sqrt 함수만 가져옴
#sqrt(4.0)


######################################################################

"""
# 날짜
import time

print(time.asctime())
"""


"""
# 다섯자리 String 찾기

a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india']
b = []

for i in a :
    if len(i) == 5 :
        b.append(i)

print(b)
"""


"""
import random

for i in range(3) :
    x = int(random.randint(1,6))
    y = int(random.randint(1,6))
    print( x, y )

"""
    


"""
sum = 0 

while True :
    x = int(input("숫자를 입력 -> "))
    sum = sum + x
    if x == 0 :
        print( "입력값 합은 %d 입니다." % sum )
        break

"""


"""
balance = 1000
interest_rate = 0.15
interest = 0
year = 0

while balance < 2000:
    year = year + 1
    interest = balance * interest_rate
    balance = balance + interest

print( " %d 년 걸립니다." % year)
print( "잔고는 %d 입니다." % balance )

"""
