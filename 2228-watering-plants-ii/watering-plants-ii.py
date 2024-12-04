class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        
        pointer_alice = 0
        pointer_bob = len(plants) - 1
        refill_no = 0
        alice_to_refill = capacityA  # Copying the original amount
        bob_to_refill = capacityB  # Copying the original amount

        while pointer_alice < pointer_bob:
            if capacityA >= plants[pointer_alice]:
                capacityA -= plants[pointer_alice]
            else:
                capacityA = alice_to_refill
                capacityA -= plants[pointer_alice]
                refill_no += 1
            
            pointer_alice += 1

            if capacityB >= plants[pointer_bob]:
                capacityB -= plants[pointer_bob]

            else:
                capacityB = bob_to_refill
                capacityB -= plants[pointer_bob]
                refill_no += 1
            
            pointer_bob -= 1

        if pointer_alice == pointer_bob:
            if capacityA >= capacityB:
                if capacityA >= plants[pointer_alice]:
                    capacityA -= plants[pointer_alice]
                else:
                    refill_no += 1
            else:
                if capacityB >= plants[pointer_bob]:
                    capacityB -= plants[pointer_bob]
                else:
                    refill_no += 1

        return refill_no
