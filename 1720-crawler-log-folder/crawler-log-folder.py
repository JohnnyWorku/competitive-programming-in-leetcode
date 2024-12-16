class Solution:
    def minOperations(self, logs: List[str]) -> int:
        counter = 0  # To count how many directries am I far from the main

        for path in logs:
            if counter > 0 and path == "../":  # To check if "../" appears when the directry is Main or not
                counter -= 1

            elif path != "./" and path != "../":
                counter += 1

            # else:
            #     counter += 1

        return counter 
