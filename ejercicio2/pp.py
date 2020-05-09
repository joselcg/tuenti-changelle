with  open('testOutput.txt', 'w') as fw, open('testInput.txt', 'r') as fr:
    i = 0
    j = 1
    numeroCasos = 0
    partidosCaso = 0
    partidosCasoInicial = 0
    ganadores = []
    for linea in fr:
        if i == 0:
            numeroCasos = int(linea.split(' ')[0])
        elif i == 1:
            partidosCasoInicial = int(linea.split(' ')[0])
            partidosCaso = partidosCasoInicial + 2
        elif (i % partidosCaso != 0):
            linea = linea.split(' ')
            if(linea[2].strip() == '1'):
                ganadores.append(linea[0])
            else:
                ganadores.append(linea[1])
        elif (i % partidosCaso == 0):  
            repeticiones = 0    
            ganador = '0'                                                                
            for elemento in ganadores:                                                                              
                apariciones = ganadores.count(elemento)                                                             
                if apariciones > repeticiones:                                                       
                    repeticiones = apariciones 
                    ganador = elemento
            fw.write('Case #' + str(j) + ': '+ ganador +'\n')
            del ganadores[:]
            j+=1
            partidosCaso = (partidosCasoInicial *(j)) + j + 1      
        i+=1
        print i
    repeticiones = 0    
    ganador = '0'                                                       
    for elemento in ganadores:                                                                              
                apariciones = ganadores.count(elemento)                                                             
                if apariciones > repeticiones:                                                       
                    repeticiones = apariciones 
                    ganador = elemento
    fw.write('Case #' + str(j) + ': '+ ganador +'\n')  
    
