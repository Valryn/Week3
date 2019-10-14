import Stack


def infixToPostfix(infixexpr):
    """Take a mathematical expression and reorder it into PostFix notation"""
    prec = {}
    # Establish order of operations hierarchy
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1

    opStack = Stack.Stack()
    postfixList = []
    tokenList = infixexpr.replace(" ", "")
    multitoken = ""

    # Scan through infixexpr and add operands and operators to postfixList
    for token in tokenList:
        # Add number or letter to multitoken
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            multitoken = multitoken + token
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            # Add multitoken to postfixList, then reset multitoken for next operand
            postfixList.append(multitoken)
            multitoken = ""
            # Work back through tokens to order statements inside "()" correctly
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            # Add multitoken to postfixList, then reset multitoken for next operand
            postfixList.append(multitoken)
            multitoken = ""

            while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)


# print(infixToPostfix("A * B + C * D"))
# print(infixToPostfix("( A + B )* C - ( D - E ) * ( F + G )"))
# print(infixToPostfix("(543 + 345) * 8952 - (11 - 22) * ( 21 + 12 )"))

def postfixEval(postfixExpr):
    """Evaluate the given postfix expression"""
    operandStack = Stack.Stack()
    tokenList = postfixExpr.split()

    #Scan tokenList for numbers or operators
    for token in tokenList:
        # If the token has a positive integer < 10 in it's first position, push the entire token
        if token[0] in "0123456789":
            operandStack.push(token)
        else:
            # When operator is encountered, evaluate it with the previous two operands
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token, int(operand1), int(operand2))
            operandStack.push(result)
    return operandStack.pop()


def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2


print(postfixEval(infixToPostfix("(543 + 345) * 8952 - (11 - 22) * ( 21 + 12)")))
