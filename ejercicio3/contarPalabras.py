# -*- coding: utf-8 -*-
import re
import string
import sys
import io
import operator
reload(sys)
sys.setdefaultencoding("utf-8")
frequency = {}
with  io.open('testOutput.txt', 'w', encoding='utf-8') as fw:
    with io.open('pg17013.txt', 'r', encoding='utf-8') as document_text:
        text_string = document_text.read().lower()
        text_string = text_string.replace('_', '')
        text_string = re.sub('\d','', text_string);
        match_pattern = re.compile(r'\W+', re.UNICODE).split(text_string)
        for word in match_pattern:
            if  len(word) > 2:
                count = frequency.get(word,0)
                frequency[word] = count + 1 
        sorted_x = sorted(frequency.items(), key=operator.itemgetter(0)),  
        sorted_final = sorted(sorted_x[0], key=operator.itemgetter(1), reverse=True),
        i = 0
        j = 1
        ajuste = 0
        tamano = len(frequency)
        with io.open('testInput.txt', 'r', encoding='utf-8') as text:
            for linea in text:
                if(i > 0):
                    for idx, words in enumerate(sorted_final[0]):
                        if(linea.strip().encode("utf-8") == words[0].encode("utf-8")):
                            a = 'Case #' + str(j) + ': '+ str(words[1])  + ' #'+ str(idx+1) +'\n'
                            a = a.decode('utf-8')
                            fw.write(a)  
                            j+=1
                        elif(str(linea.strip()) == str(idx+1)):
                            b = 'Case #' + str(j) + ': '+ words[0].encode("utf-8")  + ' '+ str(words[1]) +'\n'
                            b = b.decode('utf-8')
                            fw.write(b)  
                            j+=1
                        i+=1
                i+=1 
    
        