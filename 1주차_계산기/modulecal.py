# 계산
def plus(num1,num2): return num1+num2
def minus(num1,num2): return num1-num2
def multi(num1,num2): return num1*num2

# 음수
def neguNumber(num):
    for n in num:
        if "-" in n: return True
    return False

# 소수
def pointNumber(num):
    for n in num:
        if "." in n: return True
    return False
