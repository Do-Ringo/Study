n: str = input()
k: str = input()
N: int = int(n)
K: int = int(k)
A: float = K % N
a: int = int(A)
B: int = N - a
S: int = B % N
print(S)