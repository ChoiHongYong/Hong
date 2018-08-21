'''
손님들을 초대하여 파티를 계획하는 아이유는 가장 먼저 과일을 종류별로 일정한
갯수만큼씩 준비하려고 한다. 과일 리스트 중 집에 있는 과일과 추가로 준비할 과일의
리스트를 data.txt 파일과 같이 작성해 보았다. 과일 당 최소 5개씩 준비하려고 하며
과일의 1개당 가격을 조사하였습니다. 5개 이하인 과일은 5개가 되도록 사려고 할 때,
사야할 과일과 그에 드는 각각의 비용과 총비용을 출력하는 프로그램을 작성하시오.

<샘플 예>
과일명     가격     개수  
 사과      1500      5
 메론      2200      2 
 참외      1300      5
 수박      9000      3
 포도      4500      4
 망고      1990      3
 금귤      1100      1

<실행 예>

추가 구매 과일 리스트, 갯수 및 소요비용
    메론   3개       6600원
    수박   2개      18000원
    포도   1개       4500원
    망고   2개       3980원
    금귤   4개       4400원

총 구매 소요 비용 37480

'''
from fruitPurchase_sub import fruitPurchase


fp = open('data.txt', 'r')
strList = fp.read().splitlines()
fp.close()


fruitDics = {}

for fruit in strList:
    dataList = fruit.split()
    fruitDics[dataList[0]] = list(map(int, dataList[1:]))
    
    
resDics, total = fruitPurchase(fruitDics)

print("추가 구매 과일 리스트, 갯수 및 소요비용")

for item in resDics:
    print("{:>6}".format(item), end=' ')
    print("{:3d}개".format(resDics[item][0]), end=' ')
    print("{:10d}원".format(resDics[item][1]))
print("\n총 구매 소요 비용 %d" % total)

