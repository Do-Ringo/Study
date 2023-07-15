# import sys
# file = sys.stdin
file = open('input.txt')

n = int(file.readline())

for i in range(n):
    word = file.readline().strip()
    length=len(word)
    first_letter = word[0]
    last_letter = word[-1]
    print(first_letter)
    print(last_letter)
    number = 10
    if length > number:
        print(length)
