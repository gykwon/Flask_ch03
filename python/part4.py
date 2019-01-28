#1. 변수란? 데이터를 담는 메모리 공간

#2. 123+456 결과는?? 579
print(123+456)

#3. '123'+456 결과는?? 123456
print('123'+'456')

#4. 다음 중 잘못된 코드를 고르세요  print('123'* '456') ##TypeError: can't multiply sequence by non-int of type 'str'

print(1.23/4.56)

#print('123'* '456')

#5. 다음 코드를 실행 한 후 a에 담긴 데이터는 무엇인가? 5
a=10
a-=5 # a=a-5
print(a)

#6. 다음 코드가 출력하는 결과는? "Good "
a= 'Good Morning'
print('a[:4] : '+ a[:4])
print('a[4:] : '+ a[4:])
print('a[:-4] : '+ a[:-4])
print(a[0:len(a)-4])
print('a[-4:] : '+ a[-4:])
print(a[len(a)-4:])


#a[:4] = "Good"
#a[4:] = " Morning"
#a[:-4] = "Good Mor"
#a[-4:] = "ning"

#7. 다음 코드가 출력하는 결과는? 5, byte를 세는 함수는? sys.getsizeof()
print(len('안녕하세요'))

