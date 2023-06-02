p = input("Qual dos lados do triangulo você precisa descobrir? (cateto 1, cateto 2, ou hipotenusa):")
if p == "Hipotenusa":
    c1 = float(input("Digite o valor de um dos catetos:"))
    c2 = float(input("Digite o valot do outro cateto:"))
    cateto = c1**2
    cateto2 = c2**2
    t  = (cateto + cateto2)**(1/2)
    print("O valor da hipotenusa é {:.2f}.".format(t))
if p == "hipotenusa":
    c1 = float(input("Digite o valor de um dos catetos:"))
    c2 = float(input("Digite o valot do outro cateto:"))
    cateto = c1**2
    cateto2 = c2**2
    x  = (cateto + cateto2)**(1/2)
    print("O valor da hipotenusa é {:.2f}.".format(x))
if p == "Cateto 1":
    c2 = float(input("Digite o valor do outro cateto:"))
    h  = float(input("digite o valor da hipotenusa:"))
    hipotenusa = h**2
    cateto2 = c2**2
    r  = (hipotenusa-cateto2)**(1/2)
    print("O valor do cateto 1 é {:.2f}.".format(r))
if p == "cateto 1":
    c2 = float(input("Digite o valor do outro cateto:"))
    h  = float(input("digite o valor da hipotenusa:"))
    hipotenusa = h**2
    cateto2 = c2**2
    y  = (hipotenusa-cateto2)**(1/2)
    print("O valor do cateto 1 é {:.2f}.".format(y))
if p == "Cateto 2":
    c1 = float(input("Digite o valor do outro cateto:"))
    h  = float(input("Digite o valor da hipotenusa:"))
    hipotenusa = h**2
    cateto1 = c1**2
    z = (hipotenusa-cateto1)**(1/2)
    print("O valor do cateto 2 é {:.2f}.".format(z))
if p == "cateto 2":
    c1 = float(input("Digite o valor do outro cateto:"))
    h  = float(input("Digite o valor da hipotenusa:"))
    hipotenusa = h**2
    cateto1 = c1**2
    a = (hipotenusa-cateto1)**(1/2)
    print("O valor do cateto 2 é {:.2f}.".format(a))

