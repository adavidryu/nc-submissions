class Solution:

    def encode(self, strs: List[str]) -> str:
        results = []

        for s in strs:
            results.append(str(len(s)))
            results.append("#")
            results.append(s)

        return "".join(results)

    def decode(self, s: str) -> List[str]:
        results = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length =  int(s[i:j])
            results.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length

        return results
