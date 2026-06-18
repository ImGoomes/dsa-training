class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeDict = {")": "(", "]" : "[", "}" : "{"}

        for item in s: 
            if item in closeDict:
                if stack and stack[-1] == closeDict[item]:
                    stack.pop()
                else: 
                    return False
            else: 
                stack.append(item)

        
        return len(stack) == 0


            
        