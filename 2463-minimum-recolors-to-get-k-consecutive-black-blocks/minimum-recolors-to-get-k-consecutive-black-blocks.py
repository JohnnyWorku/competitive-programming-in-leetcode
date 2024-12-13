class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count = float('inf')
        i = 0
        j = k - 1

        while j < len(blocks):
            _count = 0
            for color in blocks[i: j + 1]:
                if color == 'W':
                    _count += 1

            count = min(count, _count)

            i += 1
            j += 1

        return count
