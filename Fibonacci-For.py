termos = int(input("Qual numero termo?\n"))

x = 0
y = 1

if termos == 0:
    print("Final")

else:
    print("Sequencia Fibonacci:")
    print(x)
    print(y)
    for n in range(2, termos):
        z = x + y
        x = y
        y = z
        print (z)

