a = 2
b = 10

def count(a,b):
    return a**b

if count(a,b) <= 100:
    print("Hello world")
else:
    print(count(a,b))

my_dict = {'a':5,'b':6, 'c':{'d':7,'e':8}, 'f':[1,2,3,4]}

for i in my_dict.items():
    print(i)

