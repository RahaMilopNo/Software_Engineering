from collections import Counter

def top_three(s):
    count = Counter(map(int, s))
    top_three = count.most_common(3)
    result = {k: v for k, v in sorted(top_three)}
    return result

print(top_three("723432741283931374238444812938144329841")) 
