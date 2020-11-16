# firstInput = input("전체 글자를 입력하세요. : ")
firstInput = "Hankuk University of Foreign Study"
secondInput = input("약자를 입력하세요. : ")
flag = True
findStartIndex = 0
for i in secondInput:
    if i not in firstInput:
        flag = False
        break
    else:
        a = firstInput.find(i, findStartIndex)
        findStartIndex = a
        if findStartIndex == -1:
            flag = False
            break

if flag :
    print("Yes")
else :
    print("No")