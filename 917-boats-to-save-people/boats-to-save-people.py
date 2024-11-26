class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boat = 0

        i = 0
        j = len(people) - 1

        while i <= j:
            boat += 1
            if people[i] <= limit - people[j]:
                i += 1

            j -= 1

        return boat 