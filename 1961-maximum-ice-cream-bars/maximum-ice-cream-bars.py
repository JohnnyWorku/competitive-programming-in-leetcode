class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        frequency_list = []

        for i in range(max(costs) + 1):
            frequency_list.append(0)

        for j in costs:
            frequency_list[j] += 1

        index = 0
        for k in range(max(costs) + 1):
            while frequency_list[k] > 0:
                costs[index] = k
                index += 1
                frequency_list[k] -= 1

        count = 0
        m = 0
        while coins > 0 and m < len(costs):
            if costs[m] <= coins:
                count += 1
                coins -= costs[m]
                m += 1
            else:
                m += 1

        return count

