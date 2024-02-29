"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""


def fn_hack_6(s):
    result = s
    ls = []

    for items in result:
        if items == "a":
            ls.append("1")
        
        elif items == "b" or items == "d":
            ls.append("-")
        
        elif items == "c":
            ls.append("3")
        
        
        elif items == "e":
            ls.append("5")
    
    if not ls:
        return ["0"]

    result = ls
    
    return result