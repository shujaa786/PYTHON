def add(a,b):
    print(f"{a}+{b} = {a+b}")
def sub(a,b):
    print(f"{a}-{b} = {a-b}")
def div(a,b):
    print(f"{a}/{b} = {a/b}")
def mul(a,b):
    print(f"{a}*{b} = {a*b}")


def main():
    a,b = map(int,input('enter any two number to perform calc: ').split())
    print("Choose any one option..")
    print('1. Addition')
    print('2. Subtraction')
    print('3. Divide')
    print('4. Multiply')
    op = int(input('choose any option to Calculate: '))
    if op == 1:
        add(a,b)
    elif op == 2:
        sub(a,b)
    elif op==3:
        div(a,b)
    elif op==4:
        mul(a,b)
    else:
        print('Choose option between 1-4')
    
main()
