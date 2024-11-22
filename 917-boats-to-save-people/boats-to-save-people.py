class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        boat =   0
        i = 0
        j = len(people) - 1

        # while i < j:
        #     if people[i] + people[j] <= limit:
        #         boat += 1
        #         people.pop(j)
        #         people.pop(i)
        #         i = 0
        #         j = len(people) - 1

        #     else:
        #         j -= 1

        # while people:  # If there are people left
        #     boat += 1
        #     people.pop()

        # return count

        while i <= j:

            remain = limit - people[j]
            boat += 1
            j -= 1

            if i <= j and people[i] <= remain:
                i += 1

        return boat
