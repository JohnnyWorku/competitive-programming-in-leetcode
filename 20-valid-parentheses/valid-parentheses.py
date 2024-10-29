class Solution:
   def isValid(self, s: str) -> bool:
    bracket_stack = []
    bracket_dict = {
        "(": ")",
        "{": "}",
        "[": "]"
    }

    for bracket in s:
        if bracket in bracket_dict:
            # If it's an opening bracket, push onto the stack
            bracket_stack.append(bracket)
        else:
            # If it's a closing bracket, check the stack
            if not bracket_stack:  # To checkif the sack is null or not
                return False
            # Pop from the stack and check if it matches
            top = bracket_stack.pop()
            if bracket_dict[top] != bracket:   # get the closing of that key
                return False

    # If stack is empty, all brackets were matched correctly
    return len(bracket_stack) == 0 # return True

        
        
