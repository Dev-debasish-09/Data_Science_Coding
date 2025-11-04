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

###########################################################################################################

class UserMainCode(object):
    @classmethod
    def agusticValues(cls, input1: str) -> str:
        
        def evaluate_expression(expr):
            # Split at '+' and sum the integer parts
            return sum(int(num) for num in expr.split('+'))
        
        def helper(s, n, index, current_expr):
            # Base condition: reached the last character
            if index == n - 1:
                current_expr += s[index]
                return evaluate_expression(current_expr)
            
            # Case 1: without inserting '+'
            without_plus = helper(s, n, index + 1, current_expr + s[index])
            
            # Case 2: inserting '+'
            with_plus = helper(s, n, index + 1, current_expr + s[index] + '+')
            
            return without_plus + with_plus
        
        return str(helper(input1, len(input1), 0, ""))

