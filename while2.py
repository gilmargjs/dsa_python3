#também é possivel usar a clausula else para encerra o loop while
x = 0
while x < 10:
    print('o valor de x nesta interação é  ',x)
    print('x ainda é para 10 falta ', 10 - x)
    x += 1
else:
    print('loop concluido')