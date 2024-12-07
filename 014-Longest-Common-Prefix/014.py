class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        s=strs[0]
        x=""
        for i in strs[1:]:
            while i.startswith(str(s))!=True:
                s=s[:len(s)-1]
        return s
