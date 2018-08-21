# 큰 수 찾기 기능
#
# @param		inputData			입력데이터(숫자)
# @return					        큰 수
def getLargeNumber(inputData):
    largeNumber = 0
    ######################여기부터 구현 (1) ---------------->
    numberStr = str(inputData)
    if len(numberStr) <= 1:
        largeNumber = inputData
    else:
        if len(numberStr) % 2 == 0:
            firstNum = numberStr[0:int(len(numberStr) / 2)]
            secondNum = numberStr[int(len(numberStr) / 2):]
        else:
            firstNum = numberStr[0:int(len(numberStr) / 2)]
            secondNum = numberStr[(int(len(numberStr) / 2)+1):]
        largeNumber = firstNum if firstNum > secondNum else secondNum
    ############################# <-------------- 여기까지 구현 (1)
    return int(largeNumber)

# 최종 숫자 구하기 기능
# 
# @param		largeNumber				큰 수
# @return								최종 숫자
def getFinaleNumber(largeNumber):
    finalNumber = 0
    ######################여기부터 구현 (2) ---------------->
    while(True):
        finalNumber = getLargeNumber(largeNumber)
        largeNumber = finalNumber
        if len(str(finalNumber)) == 1:
            break
    ############################# <-------------- 여기까지 구현 (2)
    return int(finalNumber)
