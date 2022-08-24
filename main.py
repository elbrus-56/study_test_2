a = 2
b = 10

def count(a,b):
    return a**b

if count(a,b) <= 100:
    print("Hello world")
else:
    print(count(a,b))

def rec(m):
    while m > 0:
        m -= 1
        yield m
n = iter(rec(19))

print(next(n))
print(next(n))
print(next(n))
print(next(n))

# 2 commit in Future
# Удалил словарь из второго коммита, что посмотрим что будет дальше на выходе

if a < b:
    print("True")
else:
    print("Вообще неTrue")


