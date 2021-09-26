n_entrada = int(input('Por favor, insira um número positivo: '))
snum = 0
cnum = 0
num = 2

while cnum < n_entrada:
    nprimo = True
    for i in range(2, num):
        if num % i == 0:
           nprimo = False
           break
    if nprimo:
        print(num)
        snum += num
        cnum += 1
    num += 1
print('Resultado : ',snum)