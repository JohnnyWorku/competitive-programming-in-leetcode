class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        frequency_dict = {}

        for j in costs:
            if j in frequency_dict:
                frequency_dict[j] += 1
            else:
                frequency_dict[j] = 1

        index = 0
        for k in range(max(costs) + 1):
            while frequency_dict.get(k, 0) > 0:
                costs[index] = k
                index += 1
                frequency_dict[k] -= 1

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

