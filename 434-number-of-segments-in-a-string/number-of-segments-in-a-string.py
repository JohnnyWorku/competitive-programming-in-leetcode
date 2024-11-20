class Solution:
    def countSegments(self, s: str) -> int:
        segment_list = list(s.split())
        return len(segment_list)