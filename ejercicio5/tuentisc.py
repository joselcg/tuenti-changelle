with  open('testOutput.txt', 'w') as fw, open('testInput.txt', 'r') as fr:
    i = 0
    for linea in fr:
        if i > 0:
            if ((int(linea) % 20 == 0)):
                fw.write('Case #' + str(i) + ': ' + str((int(linea) / 20))+'\n')
            else:
                resultado = int(linea) / 20;
                resto = int(linea) % 20;
                if(resto > (resultado * 9)):
                    fw.write('Case #' + str(i) + ': IMPOSSIBLE\n')
                else:
                    fw.write('Case #' + str(i) + ': ' + str(resultado)+'\n')
        i+=1