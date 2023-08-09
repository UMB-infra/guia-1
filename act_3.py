def main():
    #funcion de inicio
    
    while True:
        #presentacion del programa y solicitud de datos
        
        print('='*40)
        data = input("ingrese el numero:\t")
        #salva de data 
        safe = data
        #punto de ruptura
        if data.upper() == "EXIT":
            print('gracias por utilizar el programa')
            break
        b_i = int(input("ingrese la base:\t"))
        b_f = int(input("ingrese la base destino:\t"))
        print('='*40)
        #punto de comprovacion limites bases
        if (b_i >= 2 and b_i <= 16) and (b_f >= 2 and b_f <= 16):
            
            #obtencion de datos correctos
            test = check(data,b_i)
            
            #comprobacion de datos correctos frente a la base
            if test:
                #conversion de los datos en lista en funcion de su base
                data = clr(data)
            else:
                print(f'el numero {data}, no coincide con la base')
                continue
            
            #ciclo de seleccion de tipo de cambio
            if b_i != 10:
                if b_f != 10:
                    data = bn_b10(data,b_i)
                    dt = data
                    bina = b10_bn(data,2)
                    data = b10_bn(data,b_f)
                else:
                    data = bn_b10(data,b_i)
                    dt = data
                    bina = b10_bn(data,2)
            else:
                data = comp(data)
                dt = data
                data = b10_bn(data,b_f)
                bina = b10_bn(dt , 2)
        else:
            print('bases fuera de los limites')
            continue  
        
        #impresion de los datos      
        print(f'numero:\t{safe}\tbase:\t{b_i}')
        print(f'numero:\t{data}\tbase:\t{b_f}')
        print(f'binario:{bina}')
        print(f'acsii:\t{chr(dt)}')

def bn_b10(data,b):
    #funcion de base n a base 10
    new = 0
    #ciclo de conversion a la inversa de la lista
    for i in range(-1, -(len(data) + 1), -1):
        exp = b ** -(i + 1)
        new += int(data[i]) * exp
    
    return(new)

def b10_bn(data,b):
    #conversion de base 10 a base n
    safe = data
    new = []
    new1 = []
    while safe >= b:
        new.append(safe % b)
        safe = safe // b
    new.append(safe)
    
    #ciclo de recolocacion de los datos
    for i in range(-1, -(len(new)+1), -1):
        new1.append(str(new[i]))
    
    if b > 10:
        #transformacion de numeros a letras
        new1 = reset(new1)
    
    #remplazo de lista a un dato unico
    new = comp(new1)
    return(new)

def check(data,b):
    #funcion para comprobar que los numeros no superan el valor de la base
    safe = clr(data)
    for i in safe:
        if (int(i)+1) > b:
            return(False)
    return(True)

def comp(num1):
    num = ''
    
    #ciclo para adjuntar los datos de la lista
    for i in num1:
        num += i
    
    #seleccion si es numerico o string
    try:
        return(int(num))
    except:
        return(num)
        
def reset(num):
    num1 = []
    #ciclo para el cambio de numeros a letras
    for i in num:
        if i == '10':
            num1.append('A')
        elif i == '11':
            num1.append('B')
        elif i == '12':
            num1.append('C')
        elif i == '13':
            num1.append('D')
        elif i == '14':
            num1.append('E')
        elif i == '15':
            num1.append('F')
        else:
            num1.append(i)
    
    return(num1)

def clr(num):
    num1 = []
    #ciclo de cambio a numeros
    for i in num:
        if i.upper() == 'A':
            num1.append('10')
        elif i.upper() == 'B':
            num1.append('11')
        elif i.upper() == 'C':
            num1.append('12')
        elif i.upper() == 'D':
            num1.append('13')
        elif i.upper() == 'E':
            num1.append('14')
        elif i.upper() == 'F':
            num1.append('15')
        else:
            num1.append(i)
        
    return(num1)

#llave de apertura
if __name__ == '__main__':
    main() 