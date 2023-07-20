class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        if x < 0:
            x = -x
            neg = True
        l = [*str(x)]
        l.reverse()
        ans = int("".join(l))
        if ans > 2**31 - 1:
            return 0
        if neg == False:
            return ans
        else:
            return -ans


s = Solution()

print(s.reverse(123))
print(s.reverse(-123))
print(s.reverse(120))
