class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}
        for word in strs:
            anagram = "".join(sorted(word))
            if words.get(anagram) is None:
                words[anagram] = []
            words[anagram].append(word)
        return words.values()
        