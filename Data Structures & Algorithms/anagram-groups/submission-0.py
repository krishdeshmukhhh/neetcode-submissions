class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # Hashmap to map char count of each string to list of anagrams

        for s in strs:
            count = [0] * 26 # an array for each lower case character in the alphabet

            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)

        return list(res.values())