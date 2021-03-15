import os 
import re

class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        chars_num = len(password)
        chars_num_flag = chars_num in range(6,21)

        three_chars = [ match.group() for match in re.compile(r"([a-zA-Z\d.!])\1{2}").finditer(password)]
        three_rep_chars = len(three_chars) != 0
        
        lower_flag = 1 in [ 1 if char.isalpha() and char.islower() else 0 for char in password ] 

        upper_flag = 1 in [ 1 if char.isalpha() and char.isupper() else 0 for char in password ] 

        invalid_chars = len( re.findall(r"[^a-zA-Z\d.!]",password) ) != 0
        
        checking = True
        steps = 0
        while checking:
            if (chars_num_flag,three_rep_chars,lower_flag,upper_flag,invalid_chars) == (True,False,True,True,False):
                print(f"\nPassword '{password} is strong !\n")
                steps = 0
                checking = False
                break
        
        return steps
        
        

if __name__=="__main__":
    os.system("clear")
    password = input("Insert password to check: ")
    sol = Solution()
    print(f"\nSteps needed for password '{password}' to be strong: {sol.strongPasswordChecker(password)}\n")