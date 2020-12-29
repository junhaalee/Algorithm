class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        let, dig = [],[]
        for l in logs:
            if l.split()[1].isdigit():
                dig.append(l)
            else:
                let.append(l)

        # let.sort(key = lambda x : (x.split()[1:], x.split()[0]))
        let = sorted(let, key = lambda x : (x.split()[1:], x.split()[0]))
        
        return let+dig