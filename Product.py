# 문자열을 변경하는 기능
#
# @param		inputData		입력데이터(문자열)
# @return						변경된 문자열
def getNewStr(inputData):
    newStr = ""
    ########################여기부터 구현 (1) ---------------->
    tmpStr = ""
    for cToStr in  inputData:
        if isNum(cToStr):
            tmpStr += cToStr
        else:
            newStr += cToStr
    newStr += tmpStr
    ############################# <-------------- 여기까지 구현 (1)
    return newStr

# 상품번호를 생성하는 기능
#
# @param		newStr		변경된 문자열
# @return					상품번호
def getProductNum(newStr):
    productNum = ""
    ########################여기부터 구현 (2) ---------------->
    num = 9
    cal = 0
    for cToStr in newStr:
        if isNum(cToStr):
            cal += int(cToStr) * num
            num -= 1
    productNum = newStr + str(cal%5)
    ############################# <-------------- 여기까지 구현 (2)
    return productNum

# 숫자를 확인하는 기능 (솔루션용 기능, 제공파일에 없음)
#
# @param		num				문자
# @return						숫자인지 확인
def isNum(num):
    return str(num).isdigit()