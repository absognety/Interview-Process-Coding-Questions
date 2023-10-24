## Data Engineering Interview at Walmart

# Find the words from the given list and group them with the words which are 
# formed by different arrangements of the same letters(anagram)

# Input = ['mat','tam','cute','beat','eatb','teab','ateb']
# Output = [[“mat”, “tam”],[“cute”],[“beat”,”eatb”,”teab”,”ateb”]]

# Without using Advanced Data structures and libraries
from typing import List
def group_anagrams(words:List[str]) -> List[List[str]]:
    groups = []
    for i in range(len(words)):
        collect_groups=[]
        for j in range(i+1,len(words)):
            if sorted(words[i]) == sorted(words[j]):
                if words[i] != words[j]:
                    collect_groups.append(words[i])
                    collect_groups.append(words[j])
                else:
                    continue
        if len(collect_groups) > 0:
            groups.append(tuple(set(collect_groups)))
        else:
            groups.append((words[i],))
    result = []
    for i in range(len(groups)):
        checker = []
        for j in range(len(groups)):
            if i != j:
                if set(groups[i]).issubset(set(groups[j])):
                    checker.append(1)
                else:
                    checker.append(0)
            else:
                continue
        if (len(set(checker)) == 1) and (0 in checker):
            result.append(groups[i])
    return result

if __name__ == '__main__':
    words = list(input().strip().split(","))
    print (group_anagrams(words=words))