def fact():
    i = int(input('Факториал какого числа нам нужен?'))
    p=1
    for n in range(1,i+1):
        p *= n
    print(p)
fact()