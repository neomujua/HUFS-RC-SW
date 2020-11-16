class Stack:
    def __init__(self):
        self.classList = []

    def push(self, a):
        self.classList.append(a)
    
    def pop(self):
        return self.classList.pop()

def checkBrackets(expr):
    bracketsStack = Stack()
    for i in expr:
        if i == "(" or i=="{" or i=="[" :
            bracketsStack.push(i)
        else :
            tmpBracket = bracketsStack.pop()
            if (tmpBracket == "(" and i == ")") or (tmpBracket == "{" and i == "}") or (tmpBracket == "[" and i == "]"):
                print(f"{tmpBracket} couple with {i}")
            else :
                print("incorrect")
                break

inputBrackets = input("괄호를 입력하세요 : ")
checkBrackets(inputBrackets)