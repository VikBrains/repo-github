import sized as sized
n = 384438
m = str(n)
left = int(m[0]) + int(m[1]) + int(m[2])
right = int(m[3]) + int(m[4]) + int(m[5])
if left == right:
    print('yes')
else:
    print('no')
