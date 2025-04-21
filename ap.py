import sys

sys.stdin = open('date.txt')

print(float(1.2345e-3))
print(pow(2014.0, 14))
print(9**19 - int(float(9**19)))
x = int(input().strip())
H = int(input().strip())
M = int(input().strip())
x = x + H * 60 + M
c = x // 60
m = x % 60
print(c)
print(m)



