"""Given a string s and a list of strings dict, you need to add a closed pair of bold tag <b> and </b> to wrap the
substrings in s that exist in dict. If two such substrings overlap, you need to wrap them together by only one
pair of closed bold tag. Also, if two substrings wrapped by bold tags are consecutive, you need to combine them. """

class Solution(object):
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        for k, v in dict.items():
            