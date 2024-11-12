class Solution:
    def finalString(self, s: str) -> str:
        final_string = ""
        for letter in s:
            if letter != 'i':
                final_string += letter
            if letter == "i":
                final_string = final_string[::-1]

        return final_string
        