"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""


def fn_hack_8(s):
    result = s
    new = []
    long = len(result)
    
    if long % 2 == 0:
        for i, elm in enumerate(reversed (result), start=1):
            new.append(str(i))
        new.reverse()
    else:
        for i, elm in enumerate(reversed (result), start=1): 
            new.append(f"{elm}-{long - i + 1}")

    return new