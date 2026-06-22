class Solution:
    def isPalindrome(self, s: str) -> bool:
        palin = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        l, r = 0, len(palin)-1

        while l < r:
            if palin[r] != palin[l]:
                return False

            l += 1
            r -= 1
        
        return True

        