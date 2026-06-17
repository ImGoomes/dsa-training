class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            if s == "":
                encoded += "-;"
            else:
                encoded += f"{s};"

        return encoded

    def decode(self, s: str) -> List[str]:
        list_encoded = s.split(";")
        decoded = []

        for s in list_encoded:
            if s != "":
                if s == "-":
                    decoded.append("")
                else:    
                    decoded.append(s)
        
        return decoded