
def password_pass(n):
    result = ''
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if n % (i + j) == 0:
                result += str(i) + str(j)
    return result
n = int(input('выпало число: '))
password = password_pass(n)
if n < 3 or n > 20:
    print('ошибка! такого числа нет')
else:
    print(password)




