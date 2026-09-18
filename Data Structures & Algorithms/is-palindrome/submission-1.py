class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=re.sub(r'[^a-zA-Z0-9]', '', s)
        s=s.lower()
        revword = s[::-1]
        print(revword)
        s= list(s)
        revword=list(revword)

        for i in range(int(len(s)/2)):
            print("ogword: ")
            print(s[i])
            print("revword: ")
            print(revword[i])
            if(s[i]!= revword[i]):
                return False
        return True;