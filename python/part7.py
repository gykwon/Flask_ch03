#1. 결과가 다른것은 print(not 'ABC') > False
print(not False)
print(not 0)
print(not None)
print(not 'ABC')

#2. 결과가 True 인것은 print(True and not False)
print(True and False)
print(True and not False)
print(False and not False)

#3. 실행결과는?
a=0
if a:
    print("1")
else:
    print("2")


#4. 별찍기
for i in range(1,6):
    print('*'*i)


for i in range(1,6):
    for j in range(i):
        print('*' , end='')
    print()
#5.

for i in range(5,0,-1):
    print('*' * i)


for i in range(5,0,-1):
    for j in range(i):
        print('*', end='')
    print()



x = int(input("몇 줄 출력할까요??"))

for i in range(1,x+1):
    for j in range(i):
        print('*',end='')
    print()



y = int(input("몇 줄 출력할까??"))
for i in range(1,y+1):
    print('*' * i)
