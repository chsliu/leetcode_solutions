class Solution:
    def reverse(self, x: int):
        check = 0
        a = []
        if x < 0:
            check = 1
            x = 0-x
        x = str(x)
        b = list(x)
        for i in range(len(b), 0, -1):
            a.append(b[i-1])
        b = int(''.join(str(i) for i in a))

        if b > 2**31 - 1:
            return 0
        if check == 1:
            return -b
        else:
            return b


s = Solution()

print(s.reverse(123))
print(s.reverse(-123))
print(s.reverse(120))
