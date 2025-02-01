class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        pillow_holder = 1
        timer = 0

        while timer < time:
            if pillow_holder == 1:
                while pillow_holder < n and timer < time:
                    pillow_holder += 1
                    timer += 1

            if pillow_holder == n:
                while pillow_holder > 1 and timer < time:
                    pillow_holder -= 1
                    timer += 1

        return pillow_holder