#1. 함수호출 결과는? 3,1
def min(a,b):
    result = a

    if(a>b):
        result = b

    return result

print(min(3,4))
print(min(11,1))


#2. 옳지않은 호출 코드는? print_personnel(position='인턴')

def print_personnel(name, position='staff',nationality='Korea'):
    print('name = {0}'.format(name))
    print('position = {0}'.format(position))
    print('nationality = {0}.format(nationality')


print_personnel(name='dost')
print_personnel(name='dost',nationality='ROK')
print_personnel(name='dost',position='인턴')
print_personnel('dost',position='인턴')
#print_personnel(position='인턴')


#3. 입력받은 수의 평균을 구하는 average() 함수를 구현하세요

def average(*num):

    return sum(num) / len(num)


print(average(1,2,3,4,5,6,7,8))

#4. result의 값은 무엇인가? 이유는? None, 참인 값이 없어서
def plus_or_minus(arg):
    if arg < 0:
        return 'minus'

    elif arg > 0:
        return 'plus'


print(plus_or_minus(0))
