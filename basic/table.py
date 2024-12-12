# cline1.py
import sys

# python table.py 14

input_number = int(sys.argv[1])

for i in range(1, 21):
    #print(f'{input_number} * {i} = {input_number * i}')
    print('%d * %02d = %03d'%(input_number, i, input_number*i))
