# 풍선 이동 상태 구하기 기능
#
# @param		numberOfBalloon		입력데이터(풍선 개수)
# @param		numberOfMove		입력데이터(이동 횟수)
# @return							풍선 이동 상태
def getMoveInfo(numberOfBalloon, numberOfMove):
    moveInfo = []
    index = 1
    tmpNumberOfMove = 0 
    moveInfo.append(numberOfBalloon)
    while(True):
        if moveInfo[index - 1] > 1:
            tmpNumberOfMove += 1
            tmpNum = moveInfo[index - 1] - 2  # 결함 발생
            moveInfo[index-1] = tmpNum
            if index == len(moveInfo)-1:
                moveInfo[index] = moveInfo[index]+1
            else:
                moveInfo.append(1)
            if tmpNumberOfMove == numberOfMove:
                break
            if moveInfo[index-1] <= 1 and moveInfo[index] <= 1 :
                break
        else:
            index+= 1
    return moveInfo

# 최초 풍선 개수 구하기 기능
#
# @param		finalMoveList		최종 이동 상태
# @return                           최초 풍선 개수
def getNumber(finalMoveList):
    index = len(finalMoveList)-1
    while(True):
        if finalMoveList[index] > 0:
            finalMoveList[index] = finalMoveList[index]-1
            finalMoveList[index-1] = finalMoveList[index-1]+2  # 결함 발생
        else:
            index -= 1
        if index <= 0:
            break
    number = finalMoveList[0]
    return number