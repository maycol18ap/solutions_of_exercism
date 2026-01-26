def is_armstrong_number(number):
    '''desglose del problema'''
    n= len(str(number)) # convertimos a string para luego contar los digitos
    g= number #guardamos el numero base
    result=0 # cremaos una variable para que se vaya guardando lo sumado
    for i in range(0,n,1):
        div_result=number//10 # para ir cortando el numero
        remainder= number%10 # usamos el resudio para poder sacar el problema uno por uno
        product=remainder**n# lo elevamos a potencia
        result+= product# vamos sumando los numeros ya elevados para mas adelante
        number= div_result # cambiamos la division para avanzar con el siguiente digito
    if result==g:
        '''hacemos la prueba de T or F'''
        return True
    else: 
        return False