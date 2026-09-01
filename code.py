#1
print ("Hello")
#2
print ("Hello","World")
#3
print("Hello")
print("World")
#4
print("'Hello'")
#5
print ('"Hello World"')
#6
print('"!@#$%^&*()\'')
#7
print('"C:\\Download\\\'hello\'.py"')
#8
print ('print("Hello\\nWorld")')
#9
a=input()
print(a)
#10
n = input()
n = int(n)
print(n)
#11
f = input()
f = float(f)
print(f)
#12
x = input()
y = input()
x=int(x)
y=int(y)
print(x)
print(y)
#13
x = input()
y = input()
print(y)
print(x)
#14
x = input()
x = float(x)
print(x)
print(x)
print(x)
#15
x,y = input().split()
x=int(x)
y=int(y)
print(x)
print(y)
#16
c1, c2 = input().split()
print(c2,c1)
#17
s = input()
print(s, s, s)
#18
a, b = input().split(':')
print(a, b, sep=':')
#19
y, m, d = input().split('.')
print (d,m,y, sep='-')
#20
a,b= input ().split('-')
print(a,b,sep='')

#72
n = int(input())
while n!=0 :
  print(n)
  n = n-1

#73
n = int(input())
while n!=0 :
  print(n-1)
  n = n-1

#74
c = ord(input())
t = ord('a')
while t<=c :
  print(chr(t), end=' ')
  t += 1

#75
c=int(input())
a=0
while a!=c+1:
  print(a)
  a += 1

#76
n = int(input())
for i in range(n+1) :
  print(i)

#77
n = int(input())
s = 0
for i in range(1, n+1) :
  if i%2==0 :
    s += i
print(s)

#78
s = input()
print(s)        

while s != 'q':
    s = input()
    print(s)

#79
n = int(input())
s=0
for i in range(1, n+1) :
    s += i
    if s >= n :
        break
print(i)

#80
n,m=map(int,input().split())
for i in range(1, n+1) :
  for j in range(1, m+1) :
    print(i, j)

#81
n = int(input(),16)
for i in range(1, 16) :
  print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='')

#82
n = int(input())
for i in range(1, n + 1):
    r = i % 10 
    
    if r == 3 or r == 6 or r == 9:
        print("X", end=' ')
    else:
        print(i, end=' ')   

#83
r,g,b = map(int,input().split())
count = 0

for i in range(r) :
  for j in range(g) :
    for k in range(b) :
      print(i,j,k)
      count += 1
print(count)

#84
h, b, c, s = map(int,input().split())
t = h * b * c * s / 8 / 1024 / 1024
print(f"{t:.1f}", "MB")

#85
