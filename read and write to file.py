import re


with open('ex.txt' , 'r' , encoding='utf-8') as f:
    sum = 0
    k =0
    with open('referat2.txt', 'w', encoding='utf-8') as ff:
        for line in f:
            line = line.replace('.','!')
            ff.write(line)
            
        
