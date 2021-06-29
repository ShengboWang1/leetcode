class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        hashmap = {}
        for idx, counts_address in enumerate(cpdomains):
            left = 0
            counts = 0
            subadress = [""]
            for i in range(len(counts_address)):
                if counts_address[i] == ' ':
                    counts = int(counts_address[left: i])
                    subadress[0] = counts_address[i + 1: len(counts_address)]
                    left = i + 1

                elif counts_address[i] == '.':
                    left = i + 1
                    subadress.append(counts_address[left: len(counts_address)])

            for sub in subadress:
                if sub in hashmap:
                    hashmap[sub] += counts
                if sub not in hashmap:
                    hashmap[sub] = counts
        ans = []
        for key in hashmap.keys():
            ans.append(str(hashmap[key]) + " " + key)
        return ans