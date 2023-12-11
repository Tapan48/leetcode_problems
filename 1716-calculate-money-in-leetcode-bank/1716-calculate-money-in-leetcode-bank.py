class Solution:
    def totalMoney(self, n: int) -> int:
        a = n // 7
        nt = n % 7

        ans1 = (nt * ((2 * (a + 1)) + (nt - 1))) // 2
        ans2 = a * (2 * 28 + 7 * (a - 1)) // 2  

        return ans1 + ans2       
       