"""
generic script

text: "fooziman" output => "oozima" 
text: "barziman" output => "arzima" 
text: "qux" output => "qux" 
"""


def fn_hack_4(s):
    result = s
    change = []
    for txt in result:
        
        if txt != "f" and txt != "n" and txt != "b":
            change.append(txt)
        result= "".join(change)
    return result
print(fn_hack_4("fooziman"))
print(fn_hack_4("barziman"))
print(fn_hack_4("qux"))
