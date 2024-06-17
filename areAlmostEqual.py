class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
                # A and B are new a and b
        # after we omit the same elements
        S1 =[]
        S2 =[]
        
        # Take only the characters which are 
        # different in both the strings 
        # for every pair of indices
        for i in range(len(s1)):
        
            # If the current characters differ
            if s1[i]!= s2[i]:
                S1.append(s1[i])
                S2.append(s2[i])
                
        # The strings were already equal
        if len(S1)== len(S2)== 0:
            return True
        
        # If the lengths of the 
        # strings are two
        if len(S1)== len(S2)== 2:
        
            # If swapping these characters 
            # can make the strings equal
            if S1[0]== S1[1] and S1[0]== S1[1]:
                return True
        
        return False
        
