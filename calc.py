import math

operacao = 1
while operacao != 0 :
  operacao = input("\nDigite a operacao desejada ->\n[s]Soma \n[i]Subtracao \n[m]Multiplicacao \n[d]Divisao \n[di]Divisao inteira \n[p]Potenciacao \n[r]Raizes da funcao de segundo grau \n[rq]Raiz Quadrada \n[f]Fatorial \n[fi]Fibonacci \n[l]Log \n[pa]Progressao Aritimetica \n[sin]Seno \n[cos]Cosseno \n[tg]Tangente \n[e]Numero de Euler \n[pi]Numero Pi \n[0]Sair\n ")
  
  if operacao == "s" :

    n1 = float(input("\nDigite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    print("\nO resultado da operação é: ")
    print(n1 + n2)
  
  if operacao == "i" :

    n1 = float(input("\nDigite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    print("\nO resultado da operação é: ")
    print(n1 - n2)
  
  if operacao == "m" :

    n1 = float(input("\nDigite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    print("\nO resultado da operação é: ")
    print(n1 * n2)
  
  if operacao == "d" :
    
    n1 = float(input("\nDigite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    print("\nO resultado da operação é: ")
    print(n1 / n2)

  if operacao == "p" :
    
    n1 = float(input("\nDigite o primeiro número: "))
    n2 = float(input("Digite o segundo número (potencia): "))
    print("\nO resultado da operação é: ")
    print(n1 ** n2)

  if operacao == "di" :
    
    n1 = int(input("\nDigite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    print("\nO resultado da operação é: ")
    print(n1 // n2)

  if operacao == "r" :

    print("\nBase funcao quadratica: y=ax**2+bx+c\n")
    a = float(input("Digite o número de a: "))
    b = float(input("Digite o número de b: "))
    c = float(input("Digite o número de c: "))
    delta = (b**2) - (4*a*c)
    if delta < 0 :
      print("ERRO!! Raiz quadrada de números negativos não é computável...")
    else :
      print("\nO resultado de x1 e x2 respectivamente é: ")
      print((-b+(delta**0.5))/(2*a))
      print((-b-(delta**0.5))/(2*a))

  if operacao == "rq" :
    
    n = float(input("\nDigite o primeiro número: "))
    print("\nO resultado da operação é: ")
    print(math.sqrt(n))

  if operacao == "f" :

    numero = int(input("\nFatorial de: ") )
    resultado=1
    for n in range(1,numero+1):
      resultado *= n
      
    print("\nO resultado da operação é: ")
    print(resultado)

  if operacao == "fi" :
    
    nterm = int(input("\nQuantos termos? "))
    n1, n2 = 0, 1
    count = 0

    if nterm <= 0:
      
      print("\nDigitar um valor positivo por favor!")
      
    elif nterm == 1:
      
      print("\nSequencia de Fibonacci: ",nterm)
      print(n1)

    else:
      
      print("\nSequencia de Fibonacci: ")
      
    while count < nterm:
      print(n1)
      nth = n1 + n2
      n1 = n2
      n2 = nth
      count += 1

  if operacao == "l" :

    n = float(input("\nDigite o número: "))
    b = float(input("\nDigite a base do log: "))
    print("\nO resultado da operação é: ")
    print(math.log(n,b))

  if operacao == "pa" :

    prim = float(input("\nPrimeiro elemento: ") )
    raz = int(input("\nRazao: ") )
    n = int(input("\nQuantos elementos exibir: ") )

    ult = prim + (n-1)*raz
    ult = ult + 1
    print("\nO resultado da operação é: ")
    
    for v in range(prim, ult, raz):
      
      print(v)

  if operacao == "sin" :
    
    n = int(input("\nDigite o angulo em graus: "))
    air = math.radians(n)
    print("\nO resultado da operação é: ")
    print(math.sin(air))

  if operacao == "cos" :
    
    n = int(input("\nDigite o angulo em graus: "))
    air = math.radians(n)
    print("\nO resultado da operação é: ")
    print(math.cos(air))

  if operacao == "tg" :
    
    n = int(input("\nDigite o angulo em graus: "))
    air = math.radians(n)

    if n != 90 & n != 210:
      print("\nO resultado da operação é: ")
      print(math.tan(air))
    else :
      print("ERRO! Tangente de 90 e 210 graus não existe...")

  if operacao == "e" :

    print("\nO resultado da operação é: ")
    print(math.e)

  if operacao == "pi" :

    print("\nO resultado da operação é: ")
    print(math.pi)
  
  elif operacao == "0":
    
    break
    
print("\nSaindo da calculadora... Ate mais!")
