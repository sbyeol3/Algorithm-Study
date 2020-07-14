# 1108. Defanging an IP Address
class Solution:
    def defangIPaddr(self, address: str) -> str:
        addr = list(address)
        for i in range(len(addr)) :
            if addr[i] == '.' : addr[i] = '[.]'
        return ''.join(addr)