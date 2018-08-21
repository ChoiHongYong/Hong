#-----------------------------------------------
# 이 파일은 수정하면 안되며, 제공된 Balloon.py 파일의
# 함수를 수정해서 프로그램을 완성해야 합니다.
#-----------------------------------------------
from balloon.Balloon import *

def main():
    global numberOfMove, finalMoveList
    # 제공 데이터 세트2를 실행하려면 loadData에서 제공 데이터 세트1을 주석 처리하고제공 데이터 세트2를 주석 해제하여 실행
    inputData = loadData()

    # 풍선 이동 상태 구하기 기능
    moveInfo = getMoveInfo(inputData, numberOfMove)
    printMoveInfo(inputData, moveInfo)

    # 최초 풍선 개수 구하기 기능
    finalNum = getNumber(finalMoveList)
    printFinalNum(finalNum)


def loadData():
    global numberOfMove, finalMoveList

    ######################
    # 제공 데이터 세트 1
    ######################
    numberOfBalloon = 11
    numberOfMove = 5
    finalMoveList = [1, 1, 0, 1]



    ######################
    # 제공 데이터 세트 2
    ######################

    # numberOfBalloon = 21
    # numberOfMove = 8
    # finalMoveList = [1, 1, 1, 0, 1, 1]

    return numberOfBalloon


def printMoveInfo(inputData, moveInfo) :
    print("[{}개의 풍선에 대한 \"{}차 이동\"후 이동상태]:".format(inputData, numberOfMove), end=" ")
    if(len(moveInfo) == 0):
        print("결과값이 없습니다.")
    else:
        for move in moveInfo:
            print(move, end=" ")
        print()
    printLine()


def printFinalNum(number) :
    print("[최초 풍선 개수]:", end=" ")
    if(number == 0):
        print("결과값이 없습니다.")
    else:
        print("{}개".format(number))
    printLine()

def printLine():
    print("--------------------------------------------------------------------------")

## 메인 코드 부분 ##
if __name__ == "__main__" :
    main()