# Read only region start
class UserMainCode(object):
    @classmethod
    def kingdomSaviour(cls, input1, input2, input3, input4, input5):
        """
        input1 : int -> initial power of the king
        input2 : int -> number of monsters
        input3 : List[int] -> type of each monster (0 or 1)
        input4 : List[int] -> health of each monster
        input5 : List[int] -> increment in king's power after killing each monster
        
        Expected return type : int
        """
        # Read only region end
        
        # --- Write code here ---
        
        # Separate monsters by type 0 and 1
        monsters0 = sorted([(input4[i], input5[i]) for i in range(input2) if input3[i] == 0])
        monsters1 = sorted([(input4[i], input5[i]) for i in range(input2) if input3[i] == 1])
        
        # Simulation function
        def simulate(start_type):
            power = input1
            t = start_type
            i0 = i1 = 0
            count = 0
            
            while True:
                if t == 0:
                    # Find next killable monster of type 0
                    while i0 < len(monsters0) and monsters0[i0][0] > power:
                        i0 += 1
                    if i0 == len(monsters0):
                        break
                    power += monsters0[i0][1]
                    i0 += 1
                    t = 1
                    count += 1
                else:
                    # Find next killable monster of type 1
                    while i1 < len(monsters1) and monsters1[i1][0] > power:
                        i1 += 1
                    if i1 == len(monsters1):
                        break
                    power += monsters1[i1][1]
                    i1 += 1
                    t = 0
                    count += 1
            return count
        
        # Try starting with both types and take the maximum
        return max(simulate(0), simulate(1))


###################################################
A = 1
B = 3
C = [1, 0, 1]
D = [1, 1, 2]
E = [1, 1, 1]
prev = -1
count = 0
for i in range(B):
    if D[i] <= A and C[i] != prev:
        A += E[i]
        prev = C[i]
        count += 1

print(count)
