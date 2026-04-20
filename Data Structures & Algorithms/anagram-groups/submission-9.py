class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = defaultdict(list)
        for word in strs:
            letters = [0] * 26
            for c in word:
                letters[ord(c.lower())-ord('a')] += 1
            count[tuple(letters)].append(word)

        return list(count.values())


        