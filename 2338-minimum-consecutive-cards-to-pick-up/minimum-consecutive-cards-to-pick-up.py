class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        # left = 0
        # count = float('inf')

        # while left < len(cards) - 1:
        #     for right in range(left + 1, len(cards)):
        #         if cards[left] == cards[right]:
        #             count = min(count, right - left + 1)
        #             break
            
        #     left += 1

        # return count if count != float('inf') else -1

        nums_dict = {}
        min_cards = float('inf')

        for index, card in enumerate(cards):
            if card not in nums_dict:
                nums_dict[card] = index

            else:
                difference = index - nums_dict[card]
                min_cards = min(min_cards, difference)
                nums_dict[card] = index

        return (min_cards + 1) if min_cards != float('inf') else -1
