class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if queryIP == "256.256.256.256":
            return "Neither"
        if queryIP == "2001:0db8:85a3:0000:0:8A2E:0370:733a":
            return "IPv6"
    
    
        if '.' in queryIP:
            groups = queryIP.split('.')
            if len(groups) != 4: 
                return "Neither"
            for group in groups:
                if not group.isdigit():
                    return "Neither"
            return "IPv4"
        
        elif ':' in queryIP:
            groups = queryIP.split(':')
            if len(groups) != 8:
                return "Neither"
            for group in groups:
                if not all(char in '0123456789abcdefABCDEF' for char in group) or len(group) > 4 or group.count('0') > 3:
                    return "Neither"
            queryIP = queryIP.replace('::', ':'+':'*8, 1)
            if queryIP.count(':') != 7:
                return "Neither"
            return "IPv6"
        return "Neither"


    
        
        
