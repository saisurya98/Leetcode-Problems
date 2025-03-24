class Solution:
    def romanToInt(self, s: str) -> int:
        # TC-O(N) SC-O(6)- Asympotically O(1)
        mydict = {'I': 1, "V": 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        n = len(s)
        total = 0
        for i in range(n):
            if i != n - 1 and mydict[s[i]] < mydict[s[i + 1]]:
                total -= mydict[s[i]]
            else:
                total += mydict[s[i]]

        return total
