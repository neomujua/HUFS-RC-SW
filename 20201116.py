class Stack:
    def __init__(self):
        self.brackets = []

    def push(self, a):
        self.brackets.append(a)
    
    def pop(self):
        return self.brackets.pop()

def checkBrackets(expr):
    bracketsStack = Stack()
    for i in expr:
        if i == "(" or i=="{" or i=="[" :
            bracketsStack.push(i)
        else :
            tmpBracket = bracketsStack.pop()
            if (tmpBracket == "(" and i == ")") or (tmpBracket == "{" and i == "}") or (tmpBracket == "[" and i == "]"):
                print(f"{tmpBracket} couple with f{i}")
            else :
                print("incorrect")
                break

inputBrackets = input("괄호를 입력하세요 : ")
checkBrackets(inputBrackets)