# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).


quarter = int(input('quarter=')) 

if quarter > 4 or quarter < 1: 
 print('wrong quarter') 

if quarter == 1: 
 print('y > 0') 
 print ('x > 0')

if quarter == 2: 
 print('y > 0') 
 print ('x < 0') 

if quarter == 3: 
 print('y < 0') 
 print ('x < 0') 

if quarter == 4: 
 print('y < 0') 
 print ('x > 0')
