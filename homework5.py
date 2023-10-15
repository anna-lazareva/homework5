data = input("Введите число: ")
for char in data:
    if not char.isdigit():
        print("Вы ввели не число!")
        exit()
        
fib = [0, 1]
equals = []
for i in range(int(data)):
    if fib[-1] == fib[-2]:
        l = len(fib)
        equals += [l-2, l-1]
    fib.append(fib[-1] + fib[-2])
print(fib)
if len(equals) != 0:
    print('Индексы повторяющихся элементов:')
    print(equals)
