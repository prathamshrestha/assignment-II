def parenthese(str1):
        stack  = []
        all_ip =  {"(": ")", "{": "}", "[": "]"}
        for parenthese in str1:
            if parenthese in all_ip:
                stack.append(parenthese)
            elif len(stack) == 0 or all_ip[stack.pop()] != parenthese:
                return f'Invalid'
        return f'Valid'
if __name__ == "__main__":

    print(parenthese("(){}[]"))
    print(parenthese("()[{)}"))
    print(parenthese("()"))
    print(parenthese("({(}))"))