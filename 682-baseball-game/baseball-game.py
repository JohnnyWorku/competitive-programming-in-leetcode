class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        def is_num(character: str):
            if character.startswith('-'):
                return character[1:].isdigit()
            return character.isdigit()

        for operation in operations:
            if is_num(operation):
                stack.append(int(operation))

            elif len(stack) >= 2 and operation == '+':
                summation = stack[-1] + stack[-2]
                stack.append(summation)

            elif stack and operation == 'C':
                stack.pop()

            else:
                product = stack[-1] * 2
                stack.append(product)

        output = 0
        for i in stack:
            output += i

        return output
