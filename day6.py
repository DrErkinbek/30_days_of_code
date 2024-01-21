t = int(input())
for i in range(0, t):
    s = input()
    even = ''
    odd = ''
    for _ in range(len(s)):
        if _ % 2 == 0:
            even += str(s[_])
        elif _ % 2 != 0:
            odd += str(s[_])
    print(even, odd)