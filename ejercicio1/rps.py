with  open('testOutput.txt', 'w') as fw, open('testInput.txt', 'r') as fr:
    i = 0
    for linea in fr:
        if i > 0:
            if ((linea[0] == 'R' and linea[2] == 'S') or (linea[0] == 'S' and linea[2] == 'R')):
                fw.write('Case #' + str(i) + ': R\n')
            elif ((linea[0] == 'R' and linea[2] == 'P') or (linea[0] == 'P' and linea[2] == 'R')):
                fw.write('Case #' + str(i) + ': P\n')
            elif ((linea[0] == 'S' and linea[2] == 'P') or (linea[0] == 'P' and linea[2] == 'S')):
                fw.write('Case #' + str(i) + ': S\n')
            else:
                fw.write('Case #' + str(i) + ': -\n')
        i+=1
        
    