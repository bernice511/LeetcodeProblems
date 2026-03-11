class Solution:
    def isPalindrome(self, s: str) -> bool:
        inp = re.sub(r'[^a-zA-Z0-9]','',s)
        inp = inp.lower()
        l = len(inp)
        for i in range(l//2):
            if inp[i]!=inp[l-i-1]:
                return False
        return True
