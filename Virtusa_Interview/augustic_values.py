class UserMainCode(object):
    @classmethod
    def augustic_values(cls, input1):
        n = len(input1)
        result = 0

        for mask in range(1 << (n - 1)):
            current = ""
            total = 0
            for i in range(n):
                current += input1[i]
                # split if bit set or end of string
                if (mask >> i) & 1 or i == n - 1:
                    total += int(current)
                    current = ""
            result += total
        return result


obj = UserMainCode()
print(obj.augustic_values('125'))
