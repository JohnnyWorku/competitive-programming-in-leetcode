class Solution:
    def interpret(self, command: str) -> str:
        interpreted = ""
        temp = ""
        for char in command:
            if char == "G":
                interpreted += "G"

            elif char == ")":
                if temp == "(":
                    interpreted += "o"
                else:
                    interpreted += "al"

                temp = ""

            else:
                temp += char

        return interpreted
