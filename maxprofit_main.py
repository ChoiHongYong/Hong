'''

data.txt 파일에는 일정 기간 동안 주식 가격의 변화를 작성하였다.
일정 기간 동안에서 몇 번째 날 사서 몇 번째 날 주식을 팔았을 때,
주식 한 주당 얻을 수 있는 이득이 최대인지를 알아내는 프로그램을 작성하시오.

<실행 결과>
5번째 날에 사서 8번째 날에 팔았을 때 최대 수익이 3200입니다.
4번째 날에 사서 9번째 날에 팔았을 때 최대 수익이 2800입니다.
7번째 날에 사서 11번째 날에 팔았을 때 최대 수익이 26900입니다.

'''
from maxprofit_sub import max_profit

fp = open('data.txt', 'r')
strList = fp.read().splitlines()
fp.close()


for x in strList:
    stock = list(map(int,x.split(',')))
    res = max_profit(stock)

    print("{}번째 날에 사서 {}번째 날에 팔았을 때 최대 수익이 {}입니다.".format(res[0]+1, res[1]+1, res[2]))
