class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        subString = ''
        l = 0
        left = 0

        for right in range(len(s)):
            current = s[right]
            if current in char_map and char_map[current]>=left:
                left = char_map[current]+1
            char_map[current] = right
            l = max(l, right-left+1)
        return l