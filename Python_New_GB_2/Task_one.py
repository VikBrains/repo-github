num = float(input("Введите число: "))
i = 10
n = num
while 10 * n % 10 != 0:
    n = n * 10

m = int(n)
count = 0
while m != 0:
    m = m // 10
    count +=1

print(count)

