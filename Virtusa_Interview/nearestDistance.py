class UserMainCode(object):
    @classmethod
    def nearestDistance(cls,input1,input2,input3,input4,input5):
        n = int(input1)
        h_p = list(input2)
        h_w = list(input3)
        m= int(input4)
        p_p = list(input5)

        total_distance = 0

        for pos in p_p:
            min_dis = float('inf')

            for i in range(n):
                h_start = h_p[i]
                h_end = h_p[i]+h_w[i]-1
                if h_start <= pos <= h_end:
                    dist = 0
                elif pos < h_start:
                    dist = h_start - pos
                else:
                    dist = pos - h_end
                if dist < min_dis:
                    min_dis = dist
                total_distance += min_dis
        return total_distance

obj = UserMainCode()
print(obj.nearestDistance(2,[15,43],[15,2],3,[10,4,44]))
        
