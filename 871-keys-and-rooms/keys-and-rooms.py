class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set([0])
        queue = deque([0])
        opened_rooms = 0

        while queue:
            room = queue.popleft()
            opened_rooms += 1

            for key in rooms[room]:
                if key in visited:
                    continue
                visited.add(key)
                queue.append(key)

        return opened_rooms == len(rooms)
        