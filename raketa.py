
ora = int(input('Hány órás visszaszámlálást tervez? '))
ossz = 0
for i in range(ora):
    print(f'A kilövésig {ora-i} óra van hátra.')
    megszakit = input('Megszakítja a visszaszámlálást? ')
    if megszakit == "i":
        ossz = ossz + 1
print(f'A rakéta a az idő letelte után ennyivel indult: {ossz + ora}')