def fibonacci(nn):
    if nn == 0:
        return 0
    elif nn == 1:
        return 1
    else:
        return fibonacci(nn-1) + fibonacci(nn-2)

#0
print("Fibonacci sorozat")

#1
a =float(input("a = ").replace(',' , '.'))
b =float(input("b = ").replace(',' , '.'))

#2
if a>b:
    a, b = b, a

fibjo = []

n=0
while True:
    elem = fibonacci(n)
    if elem>a and elem <=b:
        fibjo.append(elem)
    if elem>b:
        break
    n+=1

#3
tempStr = []
for item in fibjo:
    fibjo.append(elem)

kiiras = "; ".join(tempStr)
print(kiiras)

