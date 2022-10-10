import csv


def color(code):
    return f'\u001b[{code}m'


PURPLE = color(45)
BLUE = color(44)
WHITE = color(47)
GREEN = color(42)
END = color(0)


# Сгенерировать при помощи escape-символов в консоли изображение флага (Вариант 9)

for i in range(1, 4):
    print(WHITE + ' ' * 10 + BLUE + ' ' * 6 + WHITE + ' ' * 20 + END)

for i in range(1, 3):
    print(BLUE + ' ' * 36 + END)

for i in range(1, 4):
    print(WHITE + ' ' * 10 + BLUE + ' ' * 6 + WHITE + ' ' * 20 + END)

print()

# Сгенерировать в консоли повторяющийся узор

for i in range(5):
    print(WHITE + ' ' * (10 - 2 * i) + PURPLE + '  ' * (6 + 2 * i)
          + WHITE + ' ' * (10 - 2 * i) + WHITE + ' ' * (10 - 2 * i)
          + PURPLE + '  ' * (6 + 2 * i) + WHITE + ' ' * (10 - 2 * i) + END)

for i in range(5):
    print(WHITE + ' ' * (2 + 2 * i) + PURPLE + '  ' * (14 - 2 * i)
          + WHITE + ' ' * (2 + 2 * i) + WHITE + ' ' * (2 + 2 * i)
          + PURPLE + '  ' * (14 - 2 * i) + WHITE + ' ' * (2 + 2 * i) + END)

print()

# Сгенерировать в консоли график функции (1 четверти) при помощи escape-символов

for i in range(9, 0, -1):
    print(WHITE + str(i) + WHITE + ' ' * 4 * i + GREEN + ' ' * (i // i)
          + WHITE + ' ' * (36 - 4 * i) + END)

print(WHITE + '0 1 2 3 4 5 6 7 8 9' + END, '\n')

# Вычислите процентное соотношение и сформируйте в консоли диаграмму

count_200 = 0
count_200more = 0

with open('books1.csv') as csvfile:
    books = csv.reader(csvfile, delimiter=';')
    title = csvfile.readline()
    for row in books:
        if float(row[7]) >= 200:
            count_200more += 1
        else:
            count_200 += 1

books_more200 = int((count_200 / (count_200 + count_200more)) * 100)
books_200 = 100 - books_more200

print(f'Книги дешевле 200 рублей:{GREEN + " " * books_more200 + WHITE + str(books_more200) + END} %', '\n')
print(f'Книги дороже 200 рублей: {GREEN + " " * books_200 + WHITE + str(books_200) + END} %')





