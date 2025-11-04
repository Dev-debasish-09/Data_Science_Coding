import itertools
import numpy as np
class UserMainCode(object):
    @classmethod
    def Bestpart(cls,input1,input2,input3):
        sum_part = []
        my_array = np.array(input1)
        l = np.array_split(my_array,input3)
        for i in l:
            sum_part.append(sum(i))
        return min(sum_part)
    

obj = UserMainCode()
print(obj.Bestpart([5,6,6,8,2,1],6,3))


