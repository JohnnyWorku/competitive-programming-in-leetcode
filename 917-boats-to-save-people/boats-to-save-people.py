class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        count =   0
        i = 0
        j = len(people) - 1

        while i < j:
            if people[i] + people[j] <= limit:
                count += 1
                people.pop(j)
                people.pop(i)
                i = 0
                j = len(people) - 1

            else:
                j -= 1

        while people:  # If there are people left
            count += 1
            people.pop()

        return count