list =[]
print(f'Hola usuario, soy un creador de sublistas de numeros dentro de una lista ya definida que se ve asi ⏩ {list}')
print('⏬Indique cuantas sublistas quiere crear⏬')
n = int(input())
for i in range (0, n):
    print(f'\nVamos a crear la sublista número {i+1}: ')
    lis= []
    n = 0
    valores = input(f'Ingrese el elemento {n+1} (cuando termine de ingresarlos coloque -1 para pasar a la siguiente lista\n')
    while True:
        if valores.isdigit():
            lis.append(valores)
        elif valores.isdigit() == -1:
            break
        else:
            print('Eso no es un numero, por favor escriba un numero')
    list.append(lis) 

print(f'Su lista se ve asi ⏩ {list}')