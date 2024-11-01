class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        my_dict = defaultdict(list)

        for path in paths:
            dirr, *files = path.split(" ")

            for f in files:
                fname, fcontent = f.split("(")
                my_dict[fcontent].append(dirr + "/" + fname)

        ans = []
        for j in my_dict.values():
            if len(j) > 1:
                ans.append(j)

        return ans