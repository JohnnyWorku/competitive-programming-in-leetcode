class Solution:
    def reverse(self, x: int) -> int:
        reversed_x = 0
        absolute_x = abs(x)
        INT_MIN, INT_MAX = -2**31, 2**31 - 1  # 32-bit integer range

        while absolute_x > 0:
            # Pop the last digit
            digit = absolute_x % 10
            absolute_x //= 10

            # Check for overflow before appending the digit
            if (reversed_x > INT_MAX // 10) or (reversed_x == INT_MAX // 10 and digit > INT_MAX % 10):
                return 0

            # Push the digit to the reversed number
            reversed_x = reversed_x * 10 + digit

        # Apply the original sign
        return reversed_x if x > 0 else -reversed_x
