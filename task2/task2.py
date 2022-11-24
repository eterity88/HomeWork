# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

result = True

for x in [False, True]:
  for y in [False, True]:
    for z in [False, True]:
      print ('checked for: ' + 'x=' + str(x) + ' y=' + str(y) + ' z=' + str(z))
      if not(not (x or y or z)) == (not x and not y and not z):
        result = False

print('Statement checked:' + str(result))