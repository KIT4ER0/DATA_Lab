class ArrayStack:
    def __init__(self):
        self.data = []
    def size(self):
        return len(self.data)
    def is_empty(self):
        if len(self.data) == 0:
            return True
        else:
            return False
    def push(self, value):
        self.data.append(value)
        return self.data
    def pop(self):
        if self.is_empty():
            print("Underflow: Cannot pop data from an empty list")
            return None
        else:
            return self.data.pop()
    def stackTop(self):
        if self.is_empty():
            return None
        else:
            return self.data[-1]
    def printStack(self):
        print(self.data)

def is_parentheses_matching(expression):
    stack = ArrayStack()
    for i in expression:
        if i == "(":
            stack.push(i)
        elif i == ")":
            if stack.is_empty():
                print("Parentheses in "+expression+" are unmatched")
                return False
            else:
                stack.pop()
    if stack.is_empty():
        return True
    else:
        print("Parentheses in "+expression+" are unmatched")
        return False

def copyStack(stack1, stack2):
    check = ArrayStack()
    while not stack2.is_empty():
        stack2.pop()
    while not stack1.is_empty():
        x = stack1.stackTop()
        stack1.pop()
        check.push(x)
    while not check.is_empty():
        x = check.stackTop()
        check.pop()
        stack1.push(x)
        stack2.push(x)

def infixToPostfix(expression):
    stack = ArrayStack()
    postfix = ""
    operator = ["+", "-", "*", "/"]
    priority = {"+":1, "-":1, "*":2, "/":2}
    for i in expression:
        if i not in operator:
            postfix += i
        else:
            while not stack.is_empty() and (priority[stack.stackTop()] >= priority[i]):
                postfix += stack.pop()
            stack.push(i)
    while not stack.is_empty():
        postfix += stack.pop()
    return postfix

def main():
    """test 3"""
    myStack = ArrayStack()
    myStack.push(10); myStack.push(20); myStack.push(30)
    myStack.printStack()
    x = myStack.pop()
    print(x)
    myStack.pop()
    myStack.printStack()
    myStack.pop()
    print(myStack.is_empty())
    myStack.pop()

def Lab4_1():
    """test 4.1"""
    str = "(((A-B)*C))"
    result = is_parentheses_matching(str)
    print(result)

def Lab4_2():
    """test 4.2"""
    s1 = ArrayStack(); s1.push(10); s1.push(20); s1.push(30)
    s2 = ArrayStack(); s2.push(15)
    copyStack(s1, s2)
    s1.printStack()
    s2.printStack()

def Lab4_3():
    """test 4.3"""
    # exp = "A/B*C/D"
    exp = "A+B*C-D/E"
    postfix = infixToPostfix(exp)
    print("Postfix of", exp, "is", postfix)

# main()
# Lab4_1()
# Lab4_2()
# Lab4_3()
