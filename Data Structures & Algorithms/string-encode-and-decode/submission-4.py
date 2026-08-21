class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            for ch in s:
                encoded += str(ord(ch)) + ','

            encoded += '|'

        return encoded
    def decode(self, s: str) -> List[str]:
        decoded = []

        if not '|' in s:
            return []
        
        s = s[:len(s)-1]

        for st in s.split('|'):
            decoded_str = ''
            for ch in st.split(','):
                if ch != '':
                    decoded_str += chr(int(ch)) 
            
            decoded.append(decoded_str)
        return decoded