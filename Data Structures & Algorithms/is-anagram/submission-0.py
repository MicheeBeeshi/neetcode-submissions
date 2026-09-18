class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s): return False
        sorteds = "".join(sorted(s));
        sortedt = "".join(sorted(t));
        if sorteds != sortedt:
            return False;
        return True;