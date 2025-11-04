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


##############################################################################

class UserMainCode(object):
    @classmethod
    def Bestpart(cls, input1, input2, input3):
        def helper(arr, n, k, index):
            # Base case — only one partition left
            if k == 1:
                return sum(arr[index:])

            curr_sum = 0
            best = 0

            # Try all possible places to cut the array
            for i in range(index, n - k + 1):
                curr_sum += arr[i]

                # Recursive call for remaining partitions
                next_partition = helper(arr, n, k - 1, i + 1)

                # BestSum for this configuration = min of current and next segment
                best_sum = min(curr_sum, next_partition)

                # We want the maximum among all possible bestSums
                best = max(best, best_sum)

            return best

        return helper(input1, input2, input3, 0)


