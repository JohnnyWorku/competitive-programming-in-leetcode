class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        # This solution is assumed to be started after drinking the first given water so we will have equal amount of empty bottles with numBottles

        total_to_drink = numBottles
        empty_bottles = numBottles
        remaining_empty_bottles = 0

        while empty_bottles >= numExchange:
            current_to_add = empty_bottles // numExchange
            total_to_drink += current_to_add
            empty_bottles %= numExchange  # to get the remaining empty bottles
            empty_bottles += current_to_add  # to add exchanged full water bottles after drinking

        # while remaining_empty_bottles >= numExchange:
        #     total_to_drink += remaining_empty_bottles // numExchange
        #     remaining_empty_bottles //= numExchange

        return total_to_drink