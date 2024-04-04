def arithmetic_ops(op):
    num1 = int(input("input 1st number:"))
    num2 = int(input("input 2nd number:"))
    return num1, num2, op(num1, num2)

def add(num1, num2): return num1+num2

def sub(num1, num2): return num1-num2

while True:
    op = input("input operation:")
    if op == "end":
        break
    elif op == "+":
        num1, num2, ret = arithmetic_ops(add) # 정의된 함수 사용
    elif op == "-":
        num1, num2, ret = arithmetic_ops(sub)
    elif op == "*":
        num1, num2, ret = arithmetic_ops(lambda num1, num2: num1*num2)
    elif op == "/":
        num1, num2, ret = arithmetic_ops(lambda num1, num2: num1/num2)
    elif op == "%":
        num1, num2, ret = arithmetic_ops(lambda num1, num2: num1%num2)
    else:
        print("Invalid operation")
        continue 
    print(f"{num1}{op}{num2} = {ret}")  

print("Exit program")