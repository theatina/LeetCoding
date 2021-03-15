class Solution:
    def reverseWords(self, s: str) -> str:
        tokens = s.split(" ")
        tokens = list(filter(("").__ne__, tokens))
        if '' in tokens:
          tokens.remove('')
        if len(tokens) <1:
            return ""
        new_str = tokens[len(tokens)-1]
        for i in range(len(tokens)-2,-1,-1):
            new_str += " " + tokens[i]
        
        return new_str
    