class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == "": 
            return False
        
        word = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        left, right = 0, len(word)-1

        while left < right:
            last = right
            while right == last:
                if word[left] != word[right] :
                    return False
                right -= 1
            left += 1 

        return True

        