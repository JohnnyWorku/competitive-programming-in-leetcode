class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        _count = 0
        i = 0

        for j in range(k):
            if blocks[j] == 'W':
                _count += 1

        count = _count

        for l in range(k, len(blocks)):
            if blocks[i] == "W":
                _count -= 1
            i += 1

            if blocks[l] == "W":
                _count += 1

            count = min(count, _count)

        return count




        # while j < len(blocks):
        #     _count = 0
        #     for color in blocks[i: j + 1]:
        #         if color == 'W':
        #             _count += 1

        #     count = min(count, _count)

        #     if blocks[i] == 'W':
        #         count -= 1

        #     i += 1
        #     j += 1

        # return count
