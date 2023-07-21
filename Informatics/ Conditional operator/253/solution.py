a: str = input()
A: int = int(a)
B = A % 4
b = A % 100
BLA = A % 400
if B == 0 and b != 0 or BLA == 0 :
    print('YES')
else:
    print('NO')
