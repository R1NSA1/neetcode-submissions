class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for i in strs:
            sort_s = ''.join(sorted(i))
            d[sort_s].append(i)
        return list(d.values())

