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
################################################################
'''
Explanation:
The houses cover ranges:
House 1 → [15, 19]
House 2 → [43, 44]

- Person at 30 → nearest house [15,19] → distance = 11
- Person at 44 → inside [43,44] → distance = 0
- Person at 41 → nearest house [43,44] → distance = 2
Total = 11 + 0 + 1 = 12
'''

# Input data
N = 4
housePos = [8, 15, 2, 12]
widths   = [2, 3, 3, 1]
M = 5
people   = [9, 1, 11, 13, 19]

# Step 1: build house intervals [X, X + W - 1]
houses = []
for i in range(N):
    start = housePos[i]
    end = housePos[i] + widths[i] - 1
    houses.append((start, end))

# Step 2: sort houses by start position
houses.sort()

totalDist = 0

# Step 3: for each person, find nearest house
for p in people:
    minDist = float('inf')

    for L, R in houses:
        if L <= p <= R:
            minDist = 0  # inside a house
            break        # already safe
        elif p < L:
            minDist = min(minDist, L - p)
        else:  # p > R
            minDist = min(minDist, p - R)

    totalDist += minDist

print(totalDist)  # ✅ Output: 5
        
