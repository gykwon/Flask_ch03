#1. 다음중 틀린것을 고르시오 튜플은 변경이 가능한 자료형이다

#2. 다음 코드에서 a는 어떤 결과를 갖게 될까요? [1,2,3,4]
a=[1,2,3]
a.append(4)
print(a)

#3. 다음코드는 어떤 값을 갖게되나? [1,2,4,5]
a=[1,2,3,4,5]
a.pop(2)
print(a)


#4. 다음 중 올바른 튜플 선언이 아닌것은?? [1,2,3,4,5] -> list
a=1,2,3,4,5
print(type(a))
a=1,
print(type(a))
a=(1,2,3,4,5)
print(type(a))
a=[1,2,3,4,5]
print(type(a))


#5. city, latitude, longitude 의 값은?? 'Seoul', 37.541, 126.986
city,latitude, longitude = 'Seoul', 37.541, 126.986
print(city)
print(latitude)
print(longitude)

#6. 다음 코드에서 잘못된 부분을 설명하세요 튜플은 값을 변경 할 수 없음 TypeError: 'tuple' object does not support item assignment
a=(1,2,3)
print(a[0])

#7. 다음과 같은 실행 겨로가를 갖는 dic 객체를 정의하는 코드를 작성하세요
a = {'애플' : 'www.apple.com', '파이썬':'www.python.org','마이크로소프트':'www.microsoft.com'}
print(type(a))
print(a.get('애플'))
print(a.items())
