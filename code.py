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
r,g,b=map(int,input().split())
rgb = r * g * b
print(f"{rgb/8/1024/1024:.2f} MB")

#86
n = int(input())
s = 0
c = 1
while True :
  s += c
  c += 1
  if s>=n :
    break
print(s)

#87
n=int(input())
for i in range(1, n+1) :
  if i%3==0 :
    continue
  print(i, end=' ')

#88
a, d, n = map(int, input().split())
nth_term = a + (n - 1) * d
print(nth_term)

#89
a,r,n = map(int,input().split())
nth_term = a * (r ** (n - 1))
print(nth_term)

#90
a,m,d,n = map(int,input().split())
current = a
for i in range(n - 1):
    current = current * m + d

print(current)

#91
a,b,c = map(int,input().split())
def get_gcd(x, y):
    while y:
        x, y = y, x % y
    return x

lcm_ab = (a * b) // get_gcd(a, b)
final_lcm = (lcm_ab * c) // get_gcd(lcm_ab, c)

print(final_lcm)

#92
n = int(input())     
a = input().split()  

for i in range(n) :  
  a[i] = int(a[i])      

d = []                 
for i in range(24) : 
  d.append(0)       

for i in range(n) :   
  d[a[i]] += 1

for i in range(1, 24) :
  print(d[i], end=' ')

#93
n = int(input())
a = input().split()

for i in range(n-1, -1, -1):
    print(a[i], end=' ')

#94
n = int(input())
a = input().split()

min_value = int(a[0])
for i in range(1, n):
    if int(a[i]) < min_value:
        min_value = int(a[i])
 print(min_value)

#95
d=[]                        #대괄호 [ ] 를 이용해 아무것도 없는 빈 리스트 만들기
for i in range(20) :
  d.append([])         #리스트 안에 다른 리스트 추가해 넣기
  for j in range(20) : 
    d[i].append(0)    #리스트 안에 들어있는 리스트 안에 0 추가해 넣기

n = int(input())
for i in range(n) :
  x, y = input().split()
  d[int(x)][int(y)] = 1

for i in range(1, 20) :
  for j in range(1, 20) : 
    print(d[i][j], end=' ')    #공백을 두고 한 줄로 출력
  print()                          #줄 바꿈

#96
# 1. 19x19 바둑판 상황 입력받기 (1~19 인덱스를 편하게 쓰기 위해 20x20 크기로 생성)
d = [[0] * 20 for _ in range(20)]

for i in range(1, 20):
    line = list(map(int, input().split()))
    for j in range(1, 20):
        d[i][j] = line[j - 1]


n = int(input())

for _ in range(n):
    x, y = map(int, input().split())

    
    for j in range(1, 20):
        # y열 뒤집기 (x행의 모든 열 값 반전)
        d[x][j] = 1 if d[x][j] == 0 else 0
        # x행 뒤집기 (y열의 모든 행 값 반전)
        d[j][y] = 1 if d[j][y] == 0 else 0

# 4. 결과 바둑판 출력하기
for i in range(1, 20):
    for j in range(1, 20):
        print(d[i][j], end=" ")
    print()

#97
h, w = map(int, input().split())
board = [[0] * (w + 1) for _ in range(h + 1)]
n = int(input())

for _ in range(n):
    # 막대 정보를 for문 안에서 매번 입력받아야 합니다.
    l, d, x, y = map(int, input().split())

    if d == 0:
        for i in range(l):
            board[x][y + i] = 1
    elif d == 1:
        for i in range(l):
            board[x + i][y] = 1

for i in range(1, h + 1):
    for j in range(1, w + 1):
        print(board[i][j], end=" ")
    print()

#98
d = []
for i in range(10):
    d.append(list(map(int, input().split())))
x, y = 1, 1
while True:
    if d[x][y] == 2:
        d[x][y] = 9
        break

    
    d[x][y] = 9

    if d[x][y + 1] != 1:
        y += 1
    elif d[x + 1][y] != 1:
        x += 1

    else:
        break

for i in range(10):
    for j in range(10):
        print(d[i][j], end=" ")
    print()
