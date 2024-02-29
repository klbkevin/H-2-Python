"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [] output => [0] 
"""


def fn_hack_7(s):
    result = s
    ls = []
    
    for items in result:
        if items == "a":
            ls.append("1")
        
        elif items == "b":
            ls.append(2)
        
        elif items == "c":
            ls.append("3")
        
        elif items == "d":
            ls.append(4)    
        
        elif items == "e":
            ls.append("5")
    
    if not ls:
        return[0]
    
    result = ls
    
    return result
