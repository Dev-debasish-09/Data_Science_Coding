import itertools 
class UserMainCode(object):
    @classmethod
    def allenValue(cls,input1,input2,input3):
        m = len(input3)   
        if m == 0:
            return None

        candidates = []

        for subseq in itertools.combinations(input2,m):
            diffs = [input3[i]-subseq[i] for i in range(m)]
            if len(set(diffs)) == 1 and diffs[0] > 0:
                candidates.append(diffs[0]) 

        return min(candidates) if candidates else 0    

output = UserMainCode()
print(output.allenValue(3, [4,3,1,2], [7,4]))

           
