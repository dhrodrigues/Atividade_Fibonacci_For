termos = int(input("Informe quantos termos da sequencia Fibonacci deseja\n"))

#Estrutura de repetição
while(termos !=0):

    #Declaração dos primeiros numeros
    x = 0
    y = 1
    
    
    if termos == 1:
        print("\n",x)

    elif termos == 2:
        print("\n",x,"\n",y)

    elif termos == 3:
        print("\n",x,"\n",y,"\n",x+y)

    else:
        print("Sequencia Fibonacci:")
        print(x)
        print(y)

        #Loop em for onde é realizada a soma apartir do 
        for n in range(2, termos):
            z = x + y
            x = y
            y = z
            print (z)
    print("-"*20)

    termos = int(input("Digite qual a nova sequencia Fibonacci. Caso digite 0 sera encerrado o codigo\n"))
print("Tchau obrigado por utilizar esse Script")
