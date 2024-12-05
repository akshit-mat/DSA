class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x=str(x)
        f=True
        for i in range(len(x)):
            if(x[i]!=x[-1*i-1]):
                f=False
        return f
