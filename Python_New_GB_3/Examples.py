# сколько раз встречается конкретная цифра в этом списке?
sp = [55.1245, 44 ,"5ррууу55",   [95.45,0.5] , {53:  125} ]
# для цифры 5 в поискеответ будет 11 раз

s=str(sp)                   # Преобразовали в строку
result=0                    # открыть счётчик 
for sym in s:               # Проход по строке
   if sym==str(len(sp)):
       result+=1

print(s.count("у"))